cmake_minimum_required(VERSION 3.16)
project(tests)

set(CMAKE_CXX_STANDARD 20)

include_directories(
        ${CMAKE_SOURCE_DIR}/include "../")


find_package(GTest REQUIRED)
find_package(Threads REQUIRED)


add_executable(tests main.cpp)

target_link_libraries(
        tests slvs ${GTEST_LIBRARIES} Threads::Threads)
enable_testing()
add_test(tests "./tests")
