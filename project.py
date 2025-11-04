import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("vehicle.csv")
data = data.drop(columns=['Legislative District'])
#print(data.info())

missing_value = data.isnull().sum()
#print(missing_value)

duplicates = data.duplicated().sum()
#print(duplicates)

summary = data.describe()
#print(summary)

# Unique counts of categorical variables
#print(data['Make'].value_counts().head(10))
#print(data['Model Year'].value_counts().sort_index())

plt.figure(figsize=(10,6))
data['Make'].value_counts().head(10).plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Vehicle Makes', fontsize=14)
plt.xlabel('Vehicle Make')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()