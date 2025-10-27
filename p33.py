import pandas as pd

#dataframe
df = pd.DataFrame(
    {
        "Name": ["Aiman","Ayesha","Umair"],
        "Age":[33,20,19],
        "Gender":['m','f','m']
    }
)

#print(df)
print(df["Name"])

# series
ages = pd.Series([22,4,51],name="Age")
print(ages)

print()
print("Max age in df is ", df["Age"].max())
print("Min age in df is ", df["Age"].min())

print(df.describe())
