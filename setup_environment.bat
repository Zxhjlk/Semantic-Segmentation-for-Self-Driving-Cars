@echo off
echo Creating Conda environment

:: Check if Conda is installed and in PATH
where conda >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Conda not found. Please install Miniconda or Anaconda.
    pause
    exit /b 1
)

:: Create the environment
call conda create -n nn_cars python=3.9 -y

:: Activate the environment and install packages
call conda activate nn_cars
call conda install numpy scikit-learn tensorflow matplotlib ipykernel imageio -y

echo Environment nn_cars created
pause