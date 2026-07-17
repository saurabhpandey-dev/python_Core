try:
    with open('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\File_handling\\ram.txt')as f1:
        #this line is for access data where already stored
        
        with open('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\File_handling\\sita.txt','w') as f2:
            # here create the new file 
            for i in f1:
                f2.write(i) # here copy data one by one file ram.txt to file sita.txt
                
    print('Data copied!!')
except:
    print('File not found')
else:
    f2.close()
    f1.close()
    print('all file are closed')        

# these line are for checking the data are copied or not and also for access the data of sita.txt file    
try:
    f = open('C:\\Users\\Saurabh Pandey\\Desktop\\python_Core\\File_handling\\ram.txt','r')
    print('\n',f.read())
except:
    print('File Not found!!')
else:
    print('file are close!')
    f.close()