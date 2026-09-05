import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("drivers.csv")

print("Dataset loaded successfully!")
print("Shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())
print("\nColumn names:")
print(df.columns.tolist())

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nBasic statistics:")
print(df.describe())

print("\nEmployment Status:")
print(df["employment_status"].value_counts())

print("\nDrivers by Terminal:")
print(df["home_terminal"].value_counts())

print("\nCDL Class:")
print(df["cdl_class"].value_counts())

print("\nExperience Statistics:")
print(df["years_experience"].describe())

plt.figure(figsize=(8, 5))

df["home_terminal"].value_counts().plot(kind="bar")

plt.title("Number of Drivers by Home Terminal")
plt.xlabel("Home Terminal")
plt.ylabel("Number of Drivers")

plt.tight_layout()
plt.savefig("drivers_by_terminal.png")
plt.show()