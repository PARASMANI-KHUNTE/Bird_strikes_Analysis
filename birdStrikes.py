import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
filename = "Bird_strikes.csv"
df = pd.read_csv(filename)

# Preview the dataset
print("Dataset Preview:\n", df.head())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Convert FlightDate to datetime format for better manipulation
df['FlightDate'] = pd.to_datetime(df['FlightDate'])

# ------------------- Visualization Starts -------------------

# 1. Bird Strikes by Aircraft Type
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='AircraftType', palette='Set2')
plt.title('Bird Strikes by Aircraft Type')
plt.xlabel('Aircraft Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 2. Damage Severity Distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Damage', palette='viridis', order=df['Damage'].value_counts().index)
plt.title('Distribution of Damage Severity')
plt.xlabel('Damage Type')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# 3. Bird Strikes by Wildlife Size
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='WildlifeSize', palette='coolwarm', order=df['WildlifeSize'].value_counts().index)
plt.title('Bird Strikes by Wildlife Size')
plt.xlabel('Wildlife Size')
plt.ylabel('Count')
plt.show()

# 4. Effect of Bird Strikes on Aircraft
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y='Effect', palette='muted', order=df['Effect'].value_counts().index)
plt.title('Effect of Bird Strikes on Aircraft')
plt.xlabel('Count')
plt.ylabel('Effect')
plt.show()
