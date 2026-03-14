import pandas as pd

df = pd.read_json('./cars.json')
print(df.dtypes)
print(df.info())
print(df.describe(include='all'))

# Create DataFrame from a dictionary
student_dict = {
    'Name': ['Joe', 'Nat', 'Harry'],
    'Age': [20, 21, 19],
    'Marks': [85.10, 77.80, 91.54]
  }

student_df = pd.DataFrame(student_dict)

# Get the column index as an Index object
list_Index = student_df.columns
print(list_Index)

# Get the label of the first column
label = student_df.columns[0]
print(label)
print(student_df.columns[-1])

# Get the column names as a list
get_as_list = student_df.columns.tolist() # get as a list
print(get_as_list)
print(type(get_as_list))


