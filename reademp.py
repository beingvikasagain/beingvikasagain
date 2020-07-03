import mysql.connector

conn = mysql.connector.connect(host = 'localhost', database='mydb', user='root', password='Vikas@12')

if conn.is_connected():
    print("connected to mysql")

cursor = conn.cursor()
cursor.execute("select name,sal from emp")

rows = cursor.fetchall()
for row in rows:
    name,salary=row
    print(f"{name} is working with salary {salary}")


cursor.close()

conn.close()
