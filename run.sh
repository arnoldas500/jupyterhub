#!/bin/bash  
echo "Starting raspPy framework download"
conda install git https://github.com/ASRCsoft/raspPy.git
echo "Starting gcc and gfortran download"  
conda install gcc
echo "Starting xarray package download" 
conda install -c anaconda xarray=0.9.5
echo "Done! You are ready to run the raspPY framework"  
