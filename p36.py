import pandas as pd

df = pd.DataFrame(
    {
        "Name" : ['Aiman','Ayesha','Umair'],
        "Age" : [33,20,19],
        "Gender" : ['m','f','m']
    }
)

print(df)
#print(df["Name"])
# series

age = pd.Series([40,50,60,70],name="Age")
print(age)

print(age.max())
print(age.min())