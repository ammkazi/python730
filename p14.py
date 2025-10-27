# single dimension
list = ["Aiman", 33, True]
numbers = [1,4,6,8,9]
print("Aiman" in list)
print(5 in numbers)
print(5 not in numbers)

# multi dimension
ll = [[1,2,3],[4,5,6],[7,8,9]]

#print(ll[0])
#print(ll[2][1])

# iterate over a list (single dim)
for l in list:
    print(l)


#andar ki list nikalo
for l in ll:
    print(l)


# list ke andar list ke elements
for l in ll:
    for i in l:
        print(i)
    print()