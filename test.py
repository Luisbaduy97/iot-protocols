import pandas as pd
import json

df = pd.read_csv('data/sensor_data.csv')

print(df.head())

cols = df.columns.values.tolist()
row = df.iloc[0,:].values.tolist()

print(json.dumps({v: str(j) for (v, j) in zip(cols, row)}))