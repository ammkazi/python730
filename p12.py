# set 
a = {1,2,3,4,5,2,3,4}
print(a)
b = {4,5,6,7,8,4,5}
print(b)

# set operations
print(a&b) # intersection
print(a|b) # union
print(a-b) # all of a -b
print(b-a) # all of b - a 
print(a^b) # all without intersect

a.add(100)
print(a)
a.remove(1)
print(a)
