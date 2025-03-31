@echo off
echo Creating Conda environment...

:: Check if Conda is installed and in PATH
where conda >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Conda not found. Please install Miniconda or Anaconda.
    pause
    exit /b 1
)

:: Create the environment
conda create -n sem_seg_cars python=3.9 -y

:: Activate the environment and install packages
call conda activate sem_seg_cars
conda install numpy pandas scikit-learn -y
pip install some-other-package
:: Keras, tensorflow, may need cuda for running on gpu, 

echo Environment setup complete
pause