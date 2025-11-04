import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,30,40,50]

plt.bar(x,y)
plt.xlabel("x - axis")
plt.ylabel("y - axis" )
plt.title("X vs Y values")
plt.grid()
plt.show()