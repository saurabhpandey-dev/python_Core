import os

os.chdir('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\OS_module')

print(os.getcwd())

print(os.path.exists('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\OS_module\\os.txt'))
# it is use for ensuring the file is exists or not is exists return True otherwise false


if not os.path.exists('newfolder'):
    os.mkdir('newfolder')
    print('Directory created')
else:
    print('folder is alrady having')