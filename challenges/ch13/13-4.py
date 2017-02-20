class Horse():
    def __init__(self,  n, b,  r):
        self.name = n
        self.breed = b
        self.rider = r
    
class Rider():
    def __init__(self,  n):
        self.name = n

horse_rider = Rider("Jamie Robillard")
my_horse = Horse("Cindy",  "Pinto",  horse_rider)

print(my_horse.rider.name)
