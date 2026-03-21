import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# Shape of dataset
print("Shape of dataset:", df.shape)

# Display first 5 rows
print("First 5 rows of dataset:", df.head())

# Survival rate as percentage
survival_rate = df['Survived'].mean() * 100
print("Survival rate:", survival_rate, "%")

# Mean age of survivors and non-survivors
print(df.groupby('Survived')['Age'].mean())

#Histogram of passenger ages
df['Age'].dropna().hist()
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()



