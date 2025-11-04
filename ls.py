arr = [5,1,7,9,3]
print(arr)
search = int(input("Enter the element to search "))

# similar linear 
if search in arr:
    print(search ," exisit")
else:
    print(search,"does not exist")