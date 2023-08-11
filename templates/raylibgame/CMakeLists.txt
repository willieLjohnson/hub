cmake_minimum_required(VERSION 3.15)
project(REPLACE_NAME)

find_package(raylib 3.0 REQUIRED)

set(CMAKE_C_STANDARD 11)

add_executable(${PROJECT_NAME} main.c)

target_link_libraries(${PROJECT_NAME} raylib)
