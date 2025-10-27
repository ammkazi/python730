# ls contains 10,4,6,8,9
# print the min and max element without using min and max function
# min - 4
# max - 10 

ls = [9,6,10,8,4]

min = ls[0]
max = ls[0]

for l in ls:

    if (l<min):
        min = l

    if (l>max):
        max = l

print(min,max)