import os

os.chdir('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\OS_module')
stats = os.stat('os.txt')

print(stats.st_size,'bytes') # is return the size of the any file
print(stats.st_mtime) # this return the modifyed time of the file

