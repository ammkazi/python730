import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
titanic = pd.read_csv("titanic.csv")

# 1. Handle missing values
titanic["Age"].fillna(titanic["Age"].median(), inplace=True)      # Fill missing ages with median
titanic["Embarked"].fillna(titanic["Embarked"].mode()[0], inplace=True)  # Fill missing embarked with most common value
titanic.drop(columns=["Cabin"], inplace=True)                     # Drop Cabin (too many missing values)

# 2. Remove duplicates (if any)
titanic.drop_duplicates(inplace=True)

# 3. Convert data types
titanic["Pclass"] = titanic["Pclass"].astype("category")
titanic["Sex"] = titanic["Sex"].astype("category")
titanic["Embarked"] = titanic["Embarked"].astype("category")

# 4. Clean Ticket column (optional)
titanic["Ticket"] = titanic["Ticket"].astype(str).str.replace(" ", "").str.upper()

# 5. Verify cleaning
print("✅ Cleaning Complete!\n")
print("Missing values per column:\n", titanic.isnull().sum())
print("\nData types:\n", titanic.dtypes)
print("\nSample data:\n", titanic.head())
# Set style
plt.style.use('ggplot')
'''
# 1️⃣ Gender vs Survival
plt.figure(figsize=(6,4))
titanic.groupby('Sex')['Survived'].mean().plot(kind='bar', color=['lightblue','salmon'])
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.xlabel('Gender')
plt.savefig("srbg.jpeg")
plt.show()
'''
'''
# 2️⃣ Passenger Class vs Survival
plt.figure(figsize=(6,4))
titanic.groupby('Pclass')['Survived'].mean().plot(kind='bar', color=['Green','Blue','Red'])
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class')
plt.show()
'''
'''
# 3️⃣ Age Distribution
plt.figure(figsize=(8,4))
plt.hist(titanic['Age'], bins=30, color='skyblue', edgecolor='black')
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()
'''

# 5️⃣ Fare vs Survival (Boxplot)
plt.figure(figsize=(6,4))
titanic.boxplot(column='Fare', by='Survived', grid=False)
plt.title('Fare Distribution by Survival')
plt.suptitle('')
plt.xlabel('Survived')
plt.ylabel('Fare')
plt.show()