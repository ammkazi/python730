import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,4,9,16,25]

plt.plot(x,y, linestyle="dashed", marker='o', color='green')
plt.xlabel("Numbers")
plt.ylabel("Squares")
plt.title("Numbers vs Squares")
plt.grid()
plt.show()