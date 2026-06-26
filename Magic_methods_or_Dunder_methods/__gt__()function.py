class Box:
    def __init__(self, weight):
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight

    


box1 = Box(50)
box2 = Box(30)  

print(box1 > box2)  


