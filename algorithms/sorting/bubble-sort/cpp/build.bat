@echo off
REM Check if CMake is installed
where cmake >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo CMake is not installed or not in PATH. Please install CMake and add it to your PATH.
    exit /b 1
)

REM Create a build directory if it doesn't exist
if not exist build (
    mkdir build
)

REM Navigate to the build directory
cd build

REM Select the generator (MinGW or Visual Studio)
set "GENERATOR="
if "%1" == "mingw" (
    set "GENERATOR=-G "MinGW Makefiles""
) else if "%1" == "vs" (
    set "GENERATOR=-G "Visual Studio 17 2022""
) else (
    echo No generator specified. Using default.
)

REM Run CMake to generate build files for Debug configuration
cmake %GENERATOR% -DCMAKE_BUILD_TYPE=Debug ..

REM Check if CMake generation was successful
if %ERRORLEVEL% NEQ 0 (
    echo CMake generation failed.
    exit /b 1
)

REM Build the Debug configuration
if "%1" == "mingw" (
    mingw32-make
) else if "%1" == "vs" (
    echo Building with Visual Studio.
    MSBuild BubbleSort.sln /p:Configuration=Debug
) else (
    REM Default build command for unspecified generator
    cmake --build . --config Debug
)

REM Check if the Debug build was successful
if %ERRORLEVEL% NEQ 0 (
    echo Debug build failed.
    exit /b 1
)

echo Debug build succeeded.

REM Run CMake to generate build files for Release configuration
cmake %GENERATOR% -DCMAKE_BUILD_TYPE=Release ..

REM Check if CMake generation was successful
if %ERRORLEVEL% NEQ 0 (
    echo CMake generation failed.
    exit /b 1
)

REM Build the Release configuration
if "%1" == "mingw" (
    mingw32-make
) else if "%1" == "vs" (
    echo Building with Visual Studio.
    MSBuild BubbleSort.sln /p:Configuration=Release
) else (
    REM Default build command for unspecified generator
    cmake --build . --config Release
)

REM Check if the Release build was successful
if %ERRORLEVEL% NEQ 0 (
    echo Release build failed.
    exit /b 1
)

echo Release build succeeded.
