import os 

os.chdir('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\OS_module')

print(os.path.isfile('os.txt')) # it return True if given aurgument is the file and is exist
# otherwise false

print(os.path.isfile('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\OS_module')) 
# it return false becouse this is a folder