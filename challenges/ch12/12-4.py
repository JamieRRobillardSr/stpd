class Hexagon:
    def __init__(self, s):
        self.side = s       

    def calculate_perimeter(self):    
        return  6 * self.side

hex = Hexagon(4)

print("The perimeter of that hexagon is {}.".format(hex.calculate_perimeter()))


