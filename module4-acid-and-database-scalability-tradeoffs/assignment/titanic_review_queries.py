# import os
import sqlite3
import pandas as pd
# import psycopg2
# from psycopg2.extras import execute_values



df = pd.read_csv('titanic.csv')
df['Survived'].astype(bool)
df['Age'].astype(int)
df = df.rename(columns={'Siblings/Spouses Aboard':'Siblings_spouses', 'Parents/Children Aboard': 'Parents_children'})

print(df.head())
print(df.columns)
print(df.shape)


connection = sqlite3.connect('titanic_table.sqlite')
df.to_sql('titanic_table', con=connection, if_exists='replace')

cursor = connection.cursor()

# cursor.execute('SELECT * from titanic_table;')

# How many passengers survived, and how many died?

query_0 = '''
SELECT survived,
COUNT(survived)
FROM titanic_table
GROUP BY survived
'''

result_0 = cursor.execute(query_0).fetchall()
print(result_0[0][1], 'persons died \n', result_0[1][1], 'persons survived')

print('--------------')

# How many passengers were in each class?

query_1 = '''
SELECT pclass, 
COUNT(pclass)
FROM titanic_table
GROUP BY pclass
'''

result_1 = cursor.execute(query_1).fetchall()
for i in range(0,3):
    print(f'There were {result_1[i][1]} of class {result_1[i][0]}')

print('--------------')

# How many passengers survived/died within each class?  

query_2 = '''
SELECT Pclass, COUNT(Survived)
FROM titanic_table
where Survived = 1
GROUP BY Pclass;
'''
result_2 = cursor.execute(query_2).fetchall()

query_3 = '''
SELECT Pclass, COUNT(Survived)
FROM titanic_table
where Survived = 0
GROUP BY Pclass;
'''

result_3 = cursor.execute(query_3).fetchall()

for i in range(0,3):
    print(f'{result_2[i][1]} of class {result_2[i][0]} survived')
    print(f'{result_3[i][1]} of class {result_3[i][0]} died')


print('--------------')

# What was the average age of survivors vs nonsurvivors?

query_4 = '''
SELECT survived, AVG(age)
FROM titanic_table
GROUP BY (survived)
'''

result_4 = cursor.execute(query_4).fetchall()
print(f'The average age of nonsurvivors was {round(result_4[0][1],2)}')
print(f'The average age of survivors was {round(result_4[1][1],2)}')

print('--------------')

# What was the average age of each passenger class?

query_5 = '''
SELECT Pclass, AVG(Age)
FROM titanic_table
GROUP BY (Pclass)
'''

result_5 = cursor.execute(query_5).fetchall()
for i in range(0,3):
    print(f'The average age of class {result_5[i][0]} is {round(result_5[i][1],2)}.')
    
print('--------------')

# What was the average fare by passenger class? By survival?

query_6 = '''
SELECT Pclass, survived, AVG(Fare)
FROM titanic_table
GROUP BY Pclass, Survived
ORDER BY Pclass, Survived 
'''

result_6 = cursor.execute(query_6).fetchall()
for i in range(0,3):
    print(f'The average fare of class {result_6[2*i][0]}, and whom was nonsurvival is {round(result_6[2*i][2],2)}.')
    print(f'The average fare of class {result_6[2*i+1][0]}, and whom was survival is {round(result_6[2*i+1][2],2)}.')

print('--------------')

# How many siblings/spouses aboard on average, by passenger class? By survival?

query_7 = '''
SELECT Pclass, survived, AVG(Siblings_spouses)
FROM titanic_table
GROUP BY Pclass, Survived
ORDER BY Pclass, Survived 
'''

result_7 = cursor.execute(query_7).fetchall()
for i in range(0,3):
    print(f'The average siblings/spouses aboard of class {result_7[2*i][0]}, and whom was nonsurvival is {round(result_7[2*i][2],2)}.')
    print(f'The average siblings/spouses aboard of class {result_7[2*i+1][0]}, and whom was survival is {round(result_7[2*i+1][2],2)}.')




print('--------------')

# How many parents/children aboard on average, by passenger class? By survival?

query_8 = '''
SELECT Pclass, survived, AVG(Parents_children)
FROM titanic_table
GROUP BY Pclass, Survived
ORDER BY Pclass, Survived 
'''

result_8 = cursor.execute(query_8).fetchall()
for i in range(0,3):
    print(f'The average parents/children aboard of class {result_8[2*i][0]}, and whom was nonsurvival is {round(result_8[2*i][2],2)}.')
    print(f'The average parents/children aboard of class {result_8[2*i+1][0]}, and whom was survival is {round(result_8[2*i+1][2],2)}.')


print('--------------')

# Do any passengers have the same name?

query_9 = '''
SELECT COUNT(DISTINCT name)
FROM titanic_table
'''

result_9 = cursor.execute(query_9).fetchall()
print(result_9)
print(df.shape[0] - result_9[0][0], 'have the same name on board.')