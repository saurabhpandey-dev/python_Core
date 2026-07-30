import os

print(os.getcwd())
os.chdir('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\OS_module')
print(os.getcwd())

# os.rmdir('newfolder') # rmdir(location of folder)
# it remove the folder according to the location

os.rmdir('one') #if folder cannot be empty then it return OSError 
# folder mast be empty and must be avaeliable in the current working directory
# del one folder in one time