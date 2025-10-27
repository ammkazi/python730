import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","June"]
sales = [1234.34,1456.87,1967.12,1051.12,1123.34,2001.32]

plt.figure(figsize=(10,8))
plt.bar(months,sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Half Yearly Sales Report")
plt.xticks(range(0,6))
plt.yticks(range(0, 3001, 300))
plt.savefig("Sales_Report.png", dpi=300, bbox_inches='tight')
plt.savefig("Sales_Report.svg", dpi=300, bbox_inches='tight')
plt.savefig("Sales_Report.pdf", bbox_inches='tight')
plt.grid()
plt.show()