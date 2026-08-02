import os

print(os.getcwd())

os.chdir('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\OS_module')

print(os.getcwd())

print(os.listdir()) # it return current working directory's list of all files and folders

print(os.listdir('C:\\Users\\Saurabh Pandey\\Desktop'))  # here it return all directory of Desktop inside
# if we pass any folder location then it will return that foldar inside list
