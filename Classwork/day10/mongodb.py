import pymongo as p

client = p.MongoClient("mongodb://localhost:27017")

# print(client.list_database_names())

db = client['satyam']
emp = db["employee"]

data = {"empid" : 3,"ename" : "Piyush" ,"department" : "IT"}
# emp.insert_one(data)

print(list(emp.find()))