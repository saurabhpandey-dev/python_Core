def insdata():
    name = input("Enter your name : ")
    age = input("Enter age : ")

    d = {name:age}
    obj = Myclass()

    for n,a in d.items():
        obj.name = n
        obj.age = a

    print(obj.name)
    print(obj.age)
    
insdata()
