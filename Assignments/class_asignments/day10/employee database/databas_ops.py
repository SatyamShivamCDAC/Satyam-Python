import pymysql as p
class MySqlOps:
        conn = p.connect(host = "localhost",user="root",passwd = "root",database="satyam")

        @staticmethod
        def create_table():
            cursor = MySqlOps.conn.cursor()
            cursor.execute(f"CREATE table employee(empid int,ename varchar(200),esalary int);")
            cursor.close()

        @staticmethod
        def add_record(e):
            cursor = MySqlOps.conn.cursor()
            cursor.execute(f"insert into employee values({e.id},{e.name},{e.salary});")
            cursor.close()

        @staticmethod
        def update(id,column,value):
            cursor = MySqlOps.conn.cursor()
            cursor.execute(f"update employee set {column} = {value} where ID = {id};")
            cursor.close()

        @staticmethod
        def delete(id):
            cursor = MySqlOps.conn.cursor()
            cursor.execute(f"delete from employee where id = {id}")
            cursor.close()

        @staticmethod
        def display_all():
            cursor = MySqlOps.conn.cursor()
            cursor.execute("select * from employee")
            data = cursor.fetchall()
            print(data)
            cursor.close()

        @staticmethod
        def display(e):
           cursor = MySqlOps.conn.cursor()
           cursor.execute(f"select * from employee where id = {e.id}")
           cursor.close()

