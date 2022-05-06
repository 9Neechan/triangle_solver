# triangle_solver
Solvespace lib - based triangle solver with picture export

## How to build?
### 0. Be sure you are using linux (ubuntu pref.)
### 1. Follow the instruction to manually install solvespace from their github
### 2. Clone this repo
### 3. Run these commands:
#### 1) cd /usr/local/include && sed -i '1s/^/#include <string.h>\n/'
#### 2) cd /*path to this repo*/build 
#### 3) cmake ..
#### 4) make

## How to use?
##### This project is managed by script.a in /build/. Be sure it has chmod +x rights
##### You should call script with at least 5 args.
##### ex: ./script.a 3 3 4 5 myimage
##### First argument codes the way of building a trianlge 1: two sides, one angle, 2:two angles, one side, 3: three sides
##### Next three double parameters are angles and sides values, remember sides go before angles
##### The last needed parameter is a string name of image, which will be created
##### p.s. default image is png, if u want svg or pdf, write this format as a sixth argument, if you want to work with .slvs file of created triangle, write "nd" as a seventh arg.

## All images will be saved in /images/
## Inconsistent parameters will cause an error alert



##### You can also use dockerfile to build this program on any system. This way is NOT optimal, path corrections may be needed. This project and solvespace3.0 directories should be one level above the dockerfile
