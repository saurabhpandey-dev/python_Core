# Todo list created
lst = []

def show_lst():
    if len(lst) == 0:
        print("The list should be created beforehand")
        return
    else:
        for i,value in enumerate(lst,1):
            print(f"{i} : {value}")


def add_lst():
    print("What you want to do!")
    while(True):
        data = input("tell here if not press 1 :- ")
        if data == '1':
            return
        lst.append(data)
        print(f'your work {data} added')
        
    

def del_lst():
    if len(lst) == 0:  # Yeh add karo
        print("List khaali hai!")
        return
            
    print("Which list you want to delete prees the number")
    for i,value in enumerate(lst):
        print(f"{i} : {value}")
    while(True):
        choice = int(input("Enter choice :- "))
        if choice < 0 or choice >= len(lst):
            print("Galat number!")
        else:
            data = lst.pop(choice)
            print(f"{data} is deleted! ")
            show_lst()
            return
        
        
while(True):
    print("Press 1 for Show List")
    print('Press 2 for Add List')
    print('Press 3 for Del List')
    print('Press 4 for Close App')

    i = int(input("Enter your choice:- "))

    if i==1:
        show_lst()
    elif i==2:
        add_lst()
    elif i==3:
        del_lst()
    elif i==4:
        print("Bye Bye Mota bhai")
        break
    else:
        print("Enter the valid Number!")



    


    
