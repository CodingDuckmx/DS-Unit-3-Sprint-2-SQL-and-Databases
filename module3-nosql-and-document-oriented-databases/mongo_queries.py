

import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.test_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names()) # Might appear no data, because the collection has no elements.

# collection.insert_one({    # Insert a document in the collection.
#     "name": "Pikachu",
#     "level": 30,
#     "exp": 76000000000,
#     "hp": 400,
# })
print("DOCS:", collection.count_documents({})) #Select *
print(collection.count_documents({"name": "Pikachu"})) # like a WHERE clause with filter conditions

# collection.insert_one({
#     "name": "Pikachu with metadata",
#     "level": 30,
#     "exp": 76000000000,
#     "hp": 400,
#     "metadata": {
#         "a":"something",
#         "b":"something else"
#     }
# }) # can insert nested structures / documents!!!

# collection.insert_one({
#     "name": "Bulbasaur",
#     "level": 15,
#     "experience": 4000000,
#     "hp": 300,
# }) # can insert documents with different structures

print("DOCS:", collection.count_documents({})) # select *
print("PIKA DOC:", collection.count_documents({"name": "Pikachu"})) # like a WHERE clause with filter conditions
print("LOW LEVELS:", collection.count_documents({"level": {"$lt": 25}})) # like a WHERE clause with filter conditions

print("--------------")
print("INSERT MANY...")
new_documents = [
    {"name": "Snorlax", "level": 70},
    {"name": "Charmander", "level": 100},
    {"name": "Jigglypuff", "level": 50},
]
collection.insert_many(new_documents)
print("DOCS:", collection.count_documents({})) # select *
print("ANY LEVELS:", collection.count_documents({"level": {"$gt": 0}})) # like a WHERE clause with filter conditions




print('-----------------')
print('COLLECTIONS:')
print(db.list_collection_names())

'''
"How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?"
Working with MongoDB appears to be more difficult, because the structure of the data, but seems to be so much better for real-life purposes.
This nesting method using dots, may not be as intuitive as INSET, SELECT and other commands. 
'''