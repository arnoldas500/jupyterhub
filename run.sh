#!/bin/bash                                                                                                                         
                                                                                                                                    
echo "Starting gcc and gfortran download"                                                                                           
conda install gcc                                                                                                                   
echo "Starting xarray package download"                                                                                             
conda install -c anaconda xarray=0.9.5                                                                                              
                                                                                                                                    
echo "Starting raspPy framework download"                                                                                           
pip3 install git+https://github.com/ASRCsoft/raspPy.git                                                                             
                                                                                                                                    
echo "upgrading raspPy packages"                                                                                                    
pip3 install git+https://github.com/ASRCsoft/raspPy.git --upgrade                                                                   
echo "starting pull of raspPy jupyter notebook"                                                                                     
git clone https://github.com/ASRCsoft/xcite_notebooks.git                                                                           
                                                                                                                                    
echo "Done! You are ready to run the raspPY framework"
