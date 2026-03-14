import pandas as pd
df = pd.read_csv('./employee.csv')

print(df)
print('\n =================================== \n')
print(df.info())

print('\n =================================== \n')
print(df.describe())

print('\n ===============First 5==================== \n')
print(df.head())

print('\n ================Last 5=================== \n')
print(df.tail())

print('\n ================Last 5=================== \n')
print(df.index)
# print(df.index[0])
# print(df.index[1])
print('\n =============JSON DATA====================== \n')
json_df = pd.read_json('./cars.json')
print(json_df.head())
print(json_df.info())
print(json_df.describe())
