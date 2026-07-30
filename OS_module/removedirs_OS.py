import os

print(os.getcwd())
os.chdir('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\OS_module')
print(os.getcwd())

os.mkdir('newfolder')
os.makedirs('one/two/three')

print(os.listdir())

os.removedirs('newfolder')
os.removedirs('one/two/three') # it remove multi level directory if we give location like multi lavel

print(os.listdir())