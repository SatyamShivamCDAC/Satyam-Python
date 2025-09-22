import pymongo as p

class Mongo:
    client = p.MongoClient("mongodb://localhost/27017")
    db = client.satyam
    emp = db.emp


    @staticmethod
    def create_emp(id,name,salary):
        Mongo.emp.insert_one({"empid" : id, "name" : name, "salary" : salary})
        Mongo.display_all()

    @staticmethod
    def update_emp(id,esalary):
        Mongo.emp.update_one({"empid" : id}, {"$set" : {"salary" : esalary}})
        Mongo.display_all()

    @staticmethod
    def remove_emp(id):
        Mongo.emp.delete_one({"empid" : id})
        Mongo.display_all()

    @staticmethod
    def display_one(id):
        data =  Mongo.emp.find_one({"empid" : id})
        print(list(data))

    @staticmethod
    def display_all():
        data = Mongo.emp.find()
        print(list(data))
