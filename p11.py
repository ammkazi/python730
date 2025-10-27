students = {
    1: "Aiman",
    10:"Sarah",
    30:"Ayesha"
}

# update , add, delete

print(students)
students[1] = "Nawaz" 
print(students)

students[2] = "Amaan"
print(students)

del students[10]
print(students)

for k,v in students.items():
    print(k,v)