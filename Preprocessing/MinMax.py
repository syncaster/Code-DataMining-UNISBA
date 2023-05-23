import pandas as pd
import numpy as np
from sklearn import preprocessing

csv_data = pd.read_csv('shopping_data_minmax.csv')
array = csv_data.values

x = array[:, 2:5]  # ambil kolom kedua sampai kelima
y = array[:, 0:1]  # ambil kolom pertama sampai kedua

# print(csv_data)
# print(x)

dataset = pd.DataFrame({'Customer Data': array[:, 0], 'Gender': array[:, 1], 'Age': array[:, 2],
                        'Income': array[:, 3], 'Spending Score': array[:, 4]})
print('dataset sebelum normaliasi :')
print(dataset)

minMax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data = minMax.fit_transform(x)
dataset = pd.DataFrame({'Age': data[:, 0], 'Income': data[:, 1], 'Spending Score': data[:, 2]})
print('dataset setelah normalisasi: ')
print(dataset)
