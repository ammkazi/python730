t = (1,2,3,4,5,6)
u = (6,7,8,9,0)

print(t,type(t))
print(u, type(u))

x = t+u
print(x)

z = (t,u)
print(z)

for i in z:
    #print(i)
    for a in i:
        print(a, end=" ")
    print()