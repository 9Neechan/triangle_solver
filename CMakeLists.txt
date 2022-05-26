cmake_minimum_required(VERSION 3.16)
project(triangle)

set(CMAKE_CXX_STANDARD 20)

include_directories(
        ${CMAKE_SOURCE_DIR}/include)


add_executable(triangle main.cpp solve.cpp solve.h)

target_link_libraries(triangle slvs)


