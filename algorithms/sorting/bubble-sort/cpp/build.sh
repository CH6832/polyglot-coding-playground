#!/bin/bash

# Check if CMake is installed
if ! command -v cmake &> /dev/null
then
    echo "CMake is not installed or not in PATH. Please install CMake."
    exit 1
fi

# Create a build directory if it doesn't exist
if [ ! -d "build" ]; then
    mkdir build
fi

# Navigate to the build directory
cd build

# Run CMake to generate build files for Debug configuration
cmake -DCMAKE_BUILD_TYPE=Debug ..

# Check if CMake generation was successful
if [ $? -ne 0 ]; then
    echo "CMake generation failed."
    exit 1
fi

# Build the Debug configuration
cmake --build . --config Debug

# Check if the Debug build was successful
if [ $? -ne 0 ]; then
    echo "Debug build failed."
    exit 1
fi

echo "Debug build succeeded."
 
# Run CMake to generate build files for Release configuration
cmake -DCMAKE_BUILD_TYPE=Release ..

# Check if CMake generation was successful
if [ $? -ne 0 ]; then
    echo "CMake generation failed."
    exit 1
fi

# Build the Release configuration
cmake --build . --config Release

# Check if the Release build was successful
if [ $? -ne 0 ]; then
    echo "Release build failed."
    exit 1
fi

echo "Release build succeeded."
