#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <array>
#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>

#include <slvs.h>

#ifndef TRIANGLE_SOLVE_H
#define TRIANGLE_SOLVE_H
static void *CheckMalloc(size_t);
void start();
std::array<double, 6> finish();
std::array<double, 6> solve1(double, double, double);
std::array<double, 6> solve2(double, double, double);
std::array<double, 6> solve3(double, double, double);
bool CheckError(const std::array<double, 6> &res);
std::string GenerateSlvs(const std::array<double,6> &res, const char* name);
std::array<double, 6> ChooseMethodAndRun(const char* method, const char* arg1,
                                         const char* arg2, const char* arg3);

#endif //TRIANGLE_SOLVE_H
