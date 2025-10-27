# wap to accept a string from the user and  and find its length. 
# check of characted 'a' exisit in the string

str = input("Enter a string ")
print("Length of the string is ", len(str))
if('a' in str):
    print("a exist is string")
else:
    print("a doesnt exist in string")