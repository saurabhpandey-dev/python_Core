class Student:
    def __init__(self, roll_no):
        self.roll_no = roll_no

    def __eq__(self, other):
        return self.roll_no == other.roll_no

s1 = Student(10)
s2 = Student(10)

print(s1 == s2) # agar __eq__ na ho to python dono object k memory address ko
                # k compair karega aur false return karega
