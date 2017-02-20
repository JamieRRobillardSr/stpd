class Square():
    square_list = []
    def __init__(self,  s):
        self.side = s
        self.square_list.append(self)
    
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.side, self.side, self.side, self.side)
    def calculate_perimeter(self):
        return self.side * 4
    
box = Square(4)
print(box)
    
