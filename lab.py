from sqlalchemy import create_engine
from sqlalchemy import text
import pandas as pd

"""
Basic Python and Pandas program to connect to local MySQL Database
!Important!
Make sure you install: `pip install pandas sqlalchemy mysql-connector-python`
Docs: https://docs.sqlalchemy.org/en/20/tutorial/dbapi_transactions.html
"""

#? 1. Credentials:
user = 'root' # <- update to your user (same as mysql workbench)
password = 'Test%401234' # <- update to your password (same as mysql workbench)
db = 'classicmodels' # <- update the db name
host = 'localhost' # localhost or 127.0.0.1
port = '3306' # <- default port

#? 2. Connection URL:
# 'mysql+mysqlconnector://user:password@host:port/database'
url = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}'
print(url)

#? 3. Create Engine using the connection url
engine = create_engine(url)

#? 4 Read and load table to DataFrame
sql_query_order = """ SELECT orderNumber, productCode,priceEach, orderLineNumber, quantityOrdered FROM orderdetails """
SQL_Query_product = """ SELECT * FROM products; """
with engine.connect() as my_conn:
  	# Use pandas read_sql() to read data from the database into a dataframe.
      #Using Order table
 my_data1 = pd.read_sql(text(SQL_Query_product),my_conn)
 my_data = pd.read_sql(text(sql_query_order),my_conn)
  	 #print all records from table 

 print("my_data1: ", my_data1)
 print("my_data", my_data)

print(my_data.head(10))

print(my_data1.columns)

my_data.columns = my_data.columns.str.strip()
print(my_data[['productCode', 'quantityOrdered']].head(10))
#specifying the index column
my_data.set_index('productCode', inplace=True)

print(my_data.describe())
print(my_data.dtypes)

#find the number of rows and columns
print(my_data.shape) # Get the number of rows and columns
print(my_data.shape[0]) # Get the number of rows only
print(my_data.shape[1]) # Get the number of columns only
print(my_data1.shape) # Get the number of rows and columns
print(my_data1.shape[0]) # Get the number of rows only
print(my_data1.shape[1]) # Get the number of columns only
# Check for missing values.
print("\nMissing Values:")
print(my_data.isnull().sum())
print("\nMissing Values:")
print(my_data1.isnull().sum())
#Grouping and Aggregations
grouped_data1 = my_data1.groupby('productLine').agg({'quantityInStock': 'sum', 'buyPrice': 'mean'}).reset_index()
print("\nGrouped Data:")
print(grouped_data1)
#find the total amount for each order using order details table
with engine.connect() as my_conn:

    my_data1 = pd.read_sql(text(sql_query_order), my_conn)

    print("Sample of the 'orders' DataFrame:")
    print(my_data1.head())

    # Create totalCost column
    my_data1['totalCost'] = my_data1['priceEach'] * my_data1['quantityOrdered']

    # Group by orderNumber
    grouped_data1 = my_data1.groupby('orderNumber')['totalCost'].sum().reset_index()

    print(grouped_data1)