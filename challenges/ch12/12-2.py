import math

class Circle:
    def __init__(self,  d):
        self.diameter = d
        self.radius = d / 2
        self.circumference = math.pi * d
    
    def area(self):    
        return  (math.pi * self.radius * self.radius)

dish = Circle(8)

print("The area of that dish is {} inches.".format(dish.area()))


