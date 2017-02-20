class Rectangle():
    def __init__(self,  l,  w):
        self.length = l
        self.width = w
        
    def calculate_perimeter(self):
        return self.length * 2 +  self.width * 2  

class Square():
    def __init__(self,  s):
        self.side = s
        
    def calculate_perimeter(self):
        return self.side * 4

my_sqr = Square(4)
my_rec = Rectangle(6,  10)

print("My Square {} and My Rectangle {}.".format(my_sqr.calculate_perimeter(),  my_rec.calculate_perimeter()))
