import os

print(os.walk(os.getcwd())) # we can't print it directly becouse it return generator in tuple form

vars = os.walk('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\OS_module')

for var in vars:
    print(var)

print('\n')

for current_dir, list_dir, file_list in vars:
    print(current_dir)
    print(list_dir)
    print(file_list)

# output
# <generator object walk at 0x000001C2BD1E18B0>
# ('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\OS_module', [], ['chdir_OS.py', 'cwd_OS.py', 'listdir_OS.py', 'makedirs_OS.py', 'mk
# dir_OS.py', 'os.txt', 'removedirs_OS.py', 'rmdir_OS.py', 'use_OS.py', 'walk_OS.py'])