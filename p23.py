fruits = ['Mango','Straberry','Banana']
friends = ['Ali','Mujir','Amaan','Nabeel']
numbers= [1,2,3,4,5,6,7,8]

students = {1:"Aiman",2:"Asif",3:"Ahemd"}

def printList(list):
    for l in list:
        print(l)
    print()

def printDictionary(dict):
    for k,v in dict.items():
        print(k,v)
    print()


printList(fruits)
printList(friends)
printList(numbers)

printDictionary(students)