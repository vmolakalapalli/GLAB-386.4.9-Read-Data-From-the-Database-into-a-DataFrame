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
q = 'SELECT * FROM `orders`' #TODO: update table_name

with engine.connect() as conn:
    # DataFrame
    df = pd.read_sql(q, con=conn)

    # Test DataFrame
    print(df.head())
    print('==============\n')
    # ================= Challenge ==============================
    # TODO # 1 (Pandas) try other pandas functions for data discovery:
    # add your code after this line:
    print('==============\n')
    # ================= Challenge ==============================
    # TODO # 2 (SQLALCHEMY) useful functions:
    # We can execute the query using the connection object and extract the first five rows.

    # fetchone(): Will extract a single row at a time.
    # fetchmany(n): Will extract the n number of rows at a time.
    # fetchall(): Will extract all of the rows.

    # Example:
    # output = conn.execute(text("SELECT * FROM `employees`"))
    # print(output.fetchall())