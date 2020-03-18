# titanic_queries.py

import os
import sqlite3
import pandas as pd
import numpy
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import json


# Import the file with the database
DB_FILEPATH = os.path.join(os.path.dirname(__file__), '..', 'titanic.csv')

df = pd.read_csv(DB_FILEPATH)
df.Age.astype(int)

print(df.head())

# Log into the server
load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

cursor = connection.cursor()

# Table creation

table_creation_query = '''
-- CREATE TYPE IF NOT EXISTS pclass as ENUM ('1','2','3');
-- CREATE TYPE IF NOT EXISTS sex as ENUM ('male', 'female');
CREATE TABLE IF NOT EXISTS titanic_table (
id SERIAL PRIMARY KEY, 
survived INT,
class INT,
name text,
sex text,
age INT,
siblings_spouses_aboard INT,
parents_children_aboard INT,
fare FLOAT
)
'''
cursor.execute(table_creation_query)
cursor.execute('SELECT * from titanic_table;')
result = cursor.fetchall()
print('RESULT', result)


  
values = list(df.itertuples(index=False, name=None))

insertion_query = "INSERT INTO titanic_table (survived, class, name, sex, age, siblings_spouses_aboard, parents_children_aboard, fare) VALUES %s"
execute_values(cursor, insertion_query, values)









# ACTUALLY SAVE THE TRANSACTIONS
connection.commit()



