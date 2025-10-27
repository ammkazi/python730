import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_excel('titanic.xlsx')

age_sex = titanic[["Age","Sex"]]
print(age_sex)

# #print(titanic.dtypes)

# #print(titanic["Name"])
# print(titanic.info())

# # series 
# age = titanic["Age"]
# print(age)
# survived = titanic["Survived"]

# plt.scatter(age,survived)
# plt.show()