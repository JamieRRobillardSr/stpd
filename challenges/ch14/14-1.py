class Square():
    square_list = []
    def __init__(self,  s):
        self.side = s
        self.square_list.append(self)
    
    def calculate_perimeter(self):
        return self.side * 4
