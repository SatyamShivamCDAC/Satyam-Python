import pymysql as p

conn = p.connect(host = "localhost",user="root",passwd="root",database="python")

cursor = conn.cursor()
#create table
# cursor.execute("create table employee(empid int,ename varchar(200),salary int)")

#insert into table
# cursor.execute("Insert into employee values (1,'Satyam',1500000)")
# cursor.execute("Insert into employee values (2,'Shivam',200000)")
# cursor.execute("Insert into employee values (3,'Piyush',150000)")
# cursor.execute("Insert into employee values (4,'Umang',1600000)")
# cursor.execute("Insert into employee values (5,'Arbab',1500000)")

#update table
# cursor.execute("update employee set salary = 2500000 where empid = 1")

#delete row
# cursor.execute("delete from employee where empid = 3")

#display items
# cursor.execute("select * from employee")
# data = cursor.fetchall()
# print(data)

#display item
# cursor.execute("select * from employee where empid = 1")
# data = cursor.fetchall()
# print(data)

conn.commit()
conn.close()
