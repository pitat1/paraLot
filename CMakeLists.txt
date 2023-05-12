cmake_minimum_required(VERSION 3.9)
project(igc_analyzer
    LANGUAGES CXX
    VERSION 1.0.0
    DESCRIPTION "Library for fasy analyzing igc files"
)

set(CMAKE_BUILD_TYPE Debug)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if(MSVC)
    # set(CMAKE_CXX_STANDARD 14)
    add_compile_definitions(_CRT_SECURE_NO_WARNINGS)
endif(MSVC)

if(DEFINED ENV{CPPUTEST_HOME})
    message(STATUS "Using CppUTest home: $ENV{CPPUTEST_HOME}")
    set(CPPUTEST_INCLUDE_DIRS $ENV{CPPUTEST_HOME}/include)
    set(CPPUTEST_LIBRARIES $ENV{CPPUTEST_HOME}/lib)
    set(CPPUTEST_LDFLAGS CppUTest CppUTestExt)
else()
    find_package(PkgConfig REQUIRED)
    pkg_search_module(CPPUTEST REQUIRED cpputest>=3.8)
    message(STATUS "Found CppUTest version ${CPPUTEST_VERSION}")
endif()

find_package(Qt5 COMPONENTS Core Gui Widgets WebEngine REQUIRED)

link_directories(${CPPUTEST_LIBRARIES})
    
add_subdirectory(igc_analyzer)

cmake_policy(SET CMP0054 NEW)
cmake_policy(SET CMP0057 NEW)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})

