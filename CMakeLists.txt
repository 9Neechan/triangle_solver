cmake_minimum_required(VERSION 3.16)
project(triangle)

include_directories(
        ${CMAKE_SOURCE_DIR}/include)


set(CMAKE_CXX_STANDARD 20)

add_executable(triangle main.cpp solve.cpp solve.h)

target_link_libraries(triangle slvs)
