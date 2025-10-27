# list is mutable
ll = [[1,2,3],[4,5,6],[7,8,9]]
ll[0][2] = 100
ll[1][1] = 50
ll[2][2] = 1000

print(ll)

t = (5,7,9,1)
print(t)

tup = ([1,2,3],[4,5,6],[7,8,9])
print(tup)
print(tup[0][0])
print(tup[1][2])
print(tup[2][1])


# tuple is immutable 
# list is mutable 
tup[0][0] = 100
print(tup)
