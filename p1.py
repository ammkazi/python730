# find min and max without using function
ls = [8,11,19,1,4,6]

min = ls[0]
max = ls[0]

for l in ls:
    print("Current element is", l)
    if(l<min):
        print(l,"is less than", min)
        min = l
        print("New min is", min)
    print("--")

    if(l>max):
        print(l,"is greater than", max)
        max = l
        print("New max is", max)


print("\nMin element is ", min)
print("Max element is ", max)
