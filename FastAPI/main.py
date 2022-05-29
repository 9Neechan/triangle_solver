from fastapi import FastAPI, Path
from fastapi.responses import FileResponse
from enum import Enum
from python_solvespace import Entity, SolverSystem, ResultFlag
import subprocess
import os

app = FastAPI()

class SolveType(Enum):
	TWO_SIDES_AND_ANGLE = 'two-sides-and-angle'
	SIDE_WITH_2_ANGLES = 'side-with-tow-angles'
	THREE_SIDES = 'three-sides'

def solveAll(solve_type, var_a, var_b, var_c, filename):
	size = "1600x1200"

	if os.name == 'nt':
		solve_bin = "./bin/solvespace-cli.exe"
	else:
		solve_bin = 'solvespace-cli'

	sys = SolverSystem()
	wp = sys.create_2d_base()  # WorkPlate - Рабочее пространство (Подложка)

	# Создаём 3 точки в пространстве
	point_a: Entity = sys.add_point_2d(-1, 0, wp)
	point_b: Entity = sys.add_point_2d(0, 1, wp)
	point_c: Entity = sys.add_point_2d(1, 0, wp)

	# Соединяем эти 3 точки линиями
	line_a = sys.add_line_2d(point_a, point_b, wp)
	line_b = sys.add_line_2d(point_a, point_c, wp)
	line_c = sys.add_line_2d(point_b, point_c, wp)

	def try_solve(sys: SolverSystem):

		if sys.solve() == ResultFlag.OKAY:
			# Получаем координаты новых точек
			a_x, a_y = sys.params(point_a.params)
			b_x, b_y = sys.params(point_b.params)
			c_x, c_y = sys.params(point_c.params)

			# Что и на что менять в шаблоне файла для Solvespace
			replaces = {
				'POINT_A_VALUE_X': a_x,
				'POINT_A_VALUE_Y': a_y,
				'POINT_B_VALUE_X': b_x,
				'POINT_B_VALUE_Y': b_y,
				'POINT_C_VALUE_X': c_x,
				'POINT_C_VALUE_Y': c_y,
			}

			# Имена файлов
			file_tmpl = 'template.slvs'
			file_in = f'{filename}.slvs'
			file_out = f'{filename}.png'

			# Открываем сразу и файл шаблона и временной файл
			with open(file_in, 'w') as tmp, open(file_tmpl, 'r') as template:
				# Читаем построчно шаблон
				for line in template:
					# Пытаемся найти и заменить определенные слова в строке
					for what, to in replaces.items():
						line = line.replace(what, str(to))
					# Записываем измененную строку во временной файл
					tmp.write(line)

			# Готовим команду для запуска рендера (Генератора картинки)
			cmd = f'{solve_bin} thumbnail --output {file_out} --size {size} --view front {file_in}'
			# Запускаем процесс
			proc = subprocess.Popen(
				cmd.split(' '),
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE,
				env=os.environ.copy(),
				universal_newlines=True
			)
			# Получаем от него результат выполнения (Или отсылаем ему команды. Сейчас не задействовано)
			result, err = proc.communicate()
			# Код завершения процесса
			exit_code = proc.wait()

			# Удаляем временной файл
			os.unlink(file_in)

			if exit_code != 0:
				return {f"Render returns: code {exit_code}: {result}\n{err}"}
				exit(3)

			return{f"Done. Saved to \"{file_out}\""}
			exit(0)
		else:
			return{"RESULT: FAILED"}
			exit(2)

	if solve_type == SolveType.TWO_SIDES_AND_ANGLE:
	# По двум сторонам и углу между ними
		if var_c >= 180:
			return{"ERROR: Wrong parameters!"}
			exit(1)

		sys.distance(point_a, point_b, var_a, wp)
		sys.distance(point_a, point_c, var_b, wp)
		sys.angle(line_a, line_b, var_c, wp)

		try_solve(sys)

	elif solve_type == SolveType.SIDE_WITH_2_ANGLES:
		# По одной стороне и двум углам
		if var_b + var_c >= 180:
			#print(var_a, var_b, var_c)
			return{"ERROR: Wrong parameters!"}
			exit(1)

		if abs(var_b - var_c) < 0.001 and var_b <= 60.001 and var_b >= 59.99:
			var_b = 120

		if var_b > var_c:
			# Swap B and C
			x = var_b
			var_b = var_c
			var_c = x

		sys.distance(point_a, point_b, var_a, wp)
		sys.angle(line_a, line_b, var_b, wp)
		sys.angle(line_a, line_c, var_c, wp)

		try_solve(sys)

	elif solve_type == SolveType.THREE_SIDES:
		# По трем сторонам
		if var_a +var_b < var_c or \
			var_a + var_c <var_b or \
			var_b + var_c < var_a or \
			var_a == 0 or \
			var_b == 0 or \
			var_c == 0:
			return{"ERROR: Wrong parameters!"}
			exit(1)

		sys.distance(point_a, point_b, var_a, wp)
		sys.distance(point_a, point_c,var_b, wp)
		sys.distance(point_b, point_c, var_c, wp)

		try_solve(sys)

	else:
		return {'Unsupported solver type!'}
		exit(100)

@app.get("/twoSidesAndAngle/{side1}/{side2}/{angle}/{filename}")
def twoSidesAndAngle(side1: float = Path(None, description = "The length of the first side", gt=0, lt = 9999999),
			   		side2: float = Path(None, description = "The length of the second side", gt=0, lt = 9999999),
			   		angle: float = Path(None, description = "The angle value", gt=0.00001, lt=179.99999),
			   		filename: str = Path(None, description = "Name your picture")):

	solve_type = SolveType('two-sides-and-angle')
	solveAll(solve_type, side1, side2, angle, filename)

	return FileResponse(f'{filename}.png')

@app.get("/sideAndTwoAngles/{side}/{angle1}/{angle2}/{filename}")
def sideAndTwoAngles(side: float = Path(None, description = "The length of the first side", gt=0, lt = 9999999),
					 angle1: float = Path(None, description = "The angle value", gt=0.00001, lt=179.99999),
					 angle2: float = Path(None, description = "The angle value", gt=0.00001, lt=179.99999),
					 filename: str = Path(None, description = "Name your picture")):

	solve_type = SolveType('side-with-tow-angles')
	solveAll(solve_type, side, angle1, angle2, filename)

	return FileResponse(f'{filename}.png')

@app.get("/threeSides/{side1}/{side2}/{side3}/{filename}")
def threeSides(side1: float = Path(None, description = "The length of the first side", gt=0, lt = 9999999),
			   side2: float = Path(None, description = "The length of the second side", gt=0, lt = 9999999),
			   side3: float = Path(None, description = "The length of the third side", gt=0, lt = 9999999),
			   filename: str = Path(None, description = "Name your picture")):

	solve_type = SolveType('three-sides')
	solveAll(solve_type, side1, side2, side3, filename)

	return FileResponse(f'{filename}.png')
