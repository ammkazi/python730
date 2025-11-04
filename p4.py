import pandas as pd

data = pd.read_csv("titanic.csv")
#print(data)

print(data.info())

issues_summary = {
    "Shape": data.shape,
    "Missing_Values": data.isnull().sum(),
    "Duplicate_Rows": data.duplicated().sum(),
    "Data_Types": data.dtypes,
    "Sample_Records": data.head(3)
}

print(issues_summary)