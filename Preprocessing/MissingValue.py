import pandas as pd
import numpy as np

csv_data = pd.read_csv("shopping_data_missingvalue.csv")
array = csv_data.values
print(csv_data)
# print(csv_data.isnull().values.any())  # check apakah ada missing value
print(csv_data.isna().sum())  # check jumlah missing value setiap kolom

meanAge = csv_data["Age"].mean()
csv_data["Age"] = csv_data["Age"].replace(np.nan, meanAge)

meanIncome = csv_data['Annual Income (k$)'].mean()
csv_data['Annual Income (k$)'] = csv_data['Annual Income (k$)'].replace(np.nan, meanIncome)

meanScore = csv_data['Spending Score (1-100)'].mean()
csv_data['Spending Score (1-100)'] = csv_data['Spending Score (1-100)'].replace(np.nan, meanScore)

print(csv_data)
