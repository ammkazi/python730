dict = {
    1: [1,2,3],
    2:[4,5,6],
    3:[7,8,9]
}

for k,v in dict.items():
    for i in v:
        print(i, end=" ")
    print()