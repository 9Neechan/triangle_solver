#include <slvs.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <array>


#ifndef TRIANGLE_SOLVE_H
#define TRIANGLE_SOLVE_H
static void *CheckMalloc(size_t);
void start();
std::array<double, 6> finish();
std::array<double, 6> solve1(double, double, double);
std::array<double, 6> solve2(double, double, double);
std::array<double, 6> solve3(double, double, double);

#endif //TRIANGLE_SOLVE_H
