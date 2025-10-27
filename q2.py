# wap to print the list in reverse order 
# without reversing the list 

ls = [1,2,3,4,5]
print(ls)

i = len(ls) - 1
while(i>=0):
    print(ls[i],end=" ")
    i = i - 1

print()

for i in range(-1,-6,-1):
    print(ls[i] , end=" ")
# 5,4,3,2,1