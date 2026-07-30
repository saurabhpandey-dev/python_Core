import os

print(os.getcwd())
os.chdir('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\OS_module')
print(os.getcwd())

os.mkdir('newfolder') # is create only one folder in working directory

os.makedirs('one/two/three') # it create directory but in multi layar 
# folder two is inside one and three is inside two