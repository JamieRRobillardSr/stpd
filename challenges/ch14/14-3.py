class Dumby():
    pass

def is_same(obj1,  obj2):
    return obj1 is obj2

dumb1 = Dumby()
dumb2 = dumb1
dumb3 = Dumby()

print(is_same(dumb1,  dumb2))
print(is_same(dumb1,  dumb3))
