import sqlite3

#Connection  to sqlite database
connection = sqlite3.connect("employee.db")

#Create cursor object to insert records,create table
cursor = connection.cursor()

#Create table with the help of cursor
table_info = """
Create table EMPLOYEE(NAME VARCHAR(25),TEAM VARCHAR(25), DOMAIN VARCHAR(25));

"""
cursor.execute(table_info)

#Inserting records

cursor.execute('''Insert into Employee values('Divya','Data Analytics','Healthcare')''')
cursor.execute('''Insert into Employee values('Krish','Bigdata','Finance')''')
cursor.execute('''Insert into Employee values('Sunny savita','MLOPS','Healthcare')''')
cursor.execute('''Insert into Employee values('Sudhanshu Kumar','Data Analytics','Insurance')''')
cursor.execute('''Insert into Employee values('Vikash','MLOPS','Finance')''')

#Display all records

print("The inserted records are")
data = cursor.execute('''Select * from EMPLOYEE''')
for row in data:
    print(row)


# commit the changes
connection.commit()
connection.close()