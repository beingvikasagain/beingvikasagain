import mysql.connector
def delete(id):
    conn = mysql.connector.connect(host='localhost',user='root',password='Vikas@12',database='mydb')
    if conn is not None:
        print("connected to database successfully!")
    mystr = f"delete from emp where id='{id}'"
    cursor = conn.cursor()
    try:

        cursor.execute(mystr)
        conn.commit()
        print("Employee deleted!")
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

empid = int(input("Enter emp id: "))

delete(empid)
