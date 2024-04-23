cmake_minimum_required(VERSION 3.10)
project(DesignPatterns)

# Include the directories containing the header files
# include_directories(Singleton)

# Add the source files
add_executable(main design-patterns.cpp src/creational/Singleton.cpp)

# Set different output directories for Windows, macOS, and Linux
if(WIN32)
    set(OS_NAME "Windows")
    set(DEFAULT_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build_win32")
elseif(APPLE)
    set(OS_NAME "macOS")
    set(DEFAULT_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build_macos")
else()
    set(OS_NAME "Linux")
    set(DEFAULT_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/build_linux")
endif()

# Set the output directory
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${DEFAULT_OUTPUT_DIRECTORY}")

set_target_properties(main PROPERTIES
    ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin/${OS_NAME}"
    LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin/${OS_NAME}"
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin/${OS_NAME}"
)

# Enable testing
enable_testing()

# Add a test executable
add_executable(tests src/creational/tests/TestSingleton.cpp src/creational/Singleton.cpp)

# Include FetchContent module
include(FetchContent)

# Fetch Google Test
FetchContent_Declare(
    googletest
    URL https://github.com/google/googletest/archive/5376968f6948923e2411081fd9372e71a59d8e77.zip
)

# Prevent overriding the parent project's compiler/linker settings on Windows
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Fetch Google Test and make it available
FetchContent_MakeAvailable(googletest)

# Link Google Test to the test executable
target_link_libraries(tests gtest_main)

# Add the test to CTest
add_test(NAME MyTest COMMAND tests)