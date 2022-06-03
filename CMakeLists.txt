cmake_minimum_required(VERSION 3.1.0)
project(logger_benchmarks)

set(CMAKE_CXX_FLAGS "-m64 -std=c++17 -march=native" CACHE STRING "" FORCE)
set(BUILD_SHARED_LIBS "OFF")

option(ENABLE_LTO "Enable link-time optimisation" ON)

if (ENABLE_LTO)
    # CMake's INTERPROCEDURAL_OPTIMIZATION feature isn't used as it does not
    # use gcc-ranlib and gcc-ar (as recommended by
    # https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html).
    add_compile_options(-flto)
    add_link_options(-flto)
    if (CMAKE_CXX_COMPILER_ID MATCHES ".*GNU")
        find_program(GCC_AR gcc-ar)
        if (GCC_AR)
            set(CMAKE_AR ${GCC_AR})
        endif()
        find_program(GCC_RANLIB gcc-ranlib)
        if (GCC_RANLIB)
            set(CMAKE_RANLIB ${GCC_RANLIB})
        endif()
    elseif(CMAKE_CXX_COMPILER_ID MATCHES ".*Clang")
        find_program(LLVM_AR llvm-ar)
        if (LLVM_AR)
            set(CMAKE_AR ${LLVM_AR})
        endif()
        find_program(LLVM_RANLIB llvm-ranlib)
        if (LLVM_RANLIB)
            set(CMAKE_RANLIB ${LLVM_RANLIB})
        endif()
    endif()
endif()

#-------------------------------------------------------------------------------------------------------
# Set default build to release
#-------------------------------------------------------------------------------------------------------
if (NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE "Release" CACHE STRING "Choose the type of build" FORCE)
endif ()

#---------------------------------------------------------------------------------------
# Compiler config
#---------------------------------------------------------------------------------------
if (NOT CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 17)
    set(CMAKE_CXX_STANDARD_REQUIRED ON)
endif ()

#-------------------------------------------------------------------------------------------------------
# Required Packages
#-------------------------------------------------------------------------------------------------------
find_package(Threads REQUIRED)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -march=native")

#---------------------------------------------------------------------------------------
# Subdirectories
#-------------------------------------------------------------------------------------------------------
add_subdirectory(third_party/quill)
add_subdirectory(third_party/iyengar_nanolog)
add_subdirectory(third_party/reckless)
add_subdirectory(third_party/platformlab_nanolog)
add_subdirectory(third_party/g3log)
add_subdirectory(third_party/ms_binlog)
add_subdirectory(third_party/xtr)

add_subdirectory(benchmarks)
