import psycopg2
import os
from dotenv import load_dotenv

load_dotenv() #look in the .env file for env vars, and add them to the env

DB_NAME=os.getenv('DB_NAME', default='OOPS')
DB_USER=os.getenv('DB_USER', default='OOPS')
DB_PASSWORD=os.getenv('DB_PASSWORD', default='OOPS')
DB_HOST=os.getenv('DB_HOST', default='OOPS')



### Connect to ElephantSQL-hosted PostgreSQL
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print('CONNECTION:', connection)

### A "cursor", a structure to iterate over db records to perform queries
cursor = connection.cursor()
print('CURSOR:', cursor)

### An example query
cursor.execute('SELECT * from test_table;')

### Note - nothing happened yet! We need to actually *fetch* from the cursor
cursor.fetchone()

result = cursor.fetchone()
print('RESULT:', result)