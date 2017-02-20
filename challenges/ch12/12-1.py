class Apple:
    def __init__(self,  w,  c,  a, t ):
        self.weight = w
        self.color = c
        self.age = a
        self.type = t
        
mac = Apple(8,  "red",  10,  "McIntosh")

print("I have a {} {} apple that is only {} days old and weighs {} oz.".format(mac.color,  mac.type,  mac.age,  mac.weight))
