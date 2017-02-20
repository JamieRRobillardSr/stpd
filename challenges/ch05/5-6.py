# Python Sets only allow unique values
# You would use a set whenever you have alist that should
# only have unique values.
# Sets are not iterable and do not guarentee order (not indexed).
# You can use 'in' or 'not in' 
basket = {"banana",  "mango",  "orange",  "apple"
                    ,  "orange", "apple"}

a = set('abracadabra')
b = set('alacazam')

print(basket)
print(a) 
print (b)
print(a - b)
