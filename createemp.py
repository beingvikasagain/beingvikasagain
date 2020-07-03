import mysql.connector

conn = mysql.connector.connect(host='localhost', database='mydb', user='root', password='Vikas@12')

if conn.is_connected:
    print("Successfully connection!")

cursor = conn.cursor()
try:
    cursor.execute("insert into emp values(4,'Monty',15000)")
    conn.commit()
    print("Employee Added!")
except:
    conn.rollback()

cursor.close()
conn.close()
