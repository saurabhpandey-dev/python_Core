try:
    f=open('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\File_handling\\sita.txt','r')
    print(f.read())
except FileNotFoundError: # its runs when file is not found
    print('file not found') 
else:
    print('file close!! ') # if found
    f.close()
    

    