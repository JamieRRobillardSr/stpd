class Triangle:
    def __init__(self,  h,  b):
        self.height = h
        self.base = b

    def area(self):    
        return  (.5 * (self.height * self.base))

tri = Triangle(5,  6)

print("The area of that triangle is {} inches.".format(tri.area()))


