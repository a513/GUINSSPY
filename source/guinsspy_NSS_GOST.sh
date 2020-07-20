#Скоируйте папку NSS_GOST_3.52.1_Linux_x86_64 в домашний каталог
export LD_LIBRARY_PATH=~/NSS_GOST_3.52.1_Linux_x86_64:$LD_LIBRARY_PATH
export PATH=~/NSS_GOST_3.52.1_Linux_x86_64:$PATH
python3 guinsspy.py