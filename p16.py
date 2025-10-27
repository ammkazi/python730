students = {
    1:{"name": "Aiman", "age" : 33, "isMarried": True},
    2:{"name": "Ayesha", "age" : 23, "isMarried": False}
}

for k,v in students.items():
    print(k,v)
    for a,b in v.items():
        print(a,b)
    print()