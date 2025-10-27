import pandas as pd

titanic = pd.read_csv('titanic.csv')
#print(titanic.head(10))

#print(titanic.dtypes)
#print(titanic["Name"])

titanic.to_excel("titanic.xlsx", 
                 sheet_name="passengers", 
                 index=False)