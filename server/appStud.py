import mysql.connector as mc
import os

def showBorrows(username):
    val1 = os.environ['dbUser']
    val2 = os.environ['dbPwd']
    try:
        db=mc.connect(host="localhost",user=val1,password=val2)
        if (db.is_connected()):
            print('DATABASE CONNECTED SUCCESSFULLY')
            cursor=db.cursor()
            cursor.execute("use lj;")
            query = "select * from students where uname='{}';".format(username)
            cursor.execute(query)
            studDetails = cursor.fetchall()
            db.commit()
            db.close()
            print(f"Shown")
            print(studDetails)
            return studDetails
        else:
            return 1
    except Exception as e:
        print(f"Error processing request: {e}")
        return 1
    

def becomeMember(username):
    val1 = os.environ['dbUser']
    val2 = os.environ['dbPwd']
    try:
        db=mc.connect(host="localhost",user=val1,password=val2)
        if (db.is_connected()):
            print('DATABASE CONNECTED SUCCESSFULLY')
            cursor=db.cursor()
            cursor.execute("use lj;")
            query = "insert into students (uname) values ('{}');".format(username)
            cursor.execute(query)
            db.commit()
            db.close()
            print(f"Added")
            return 0
        else:
            return 1
    except Exception as e:
        print(f"Error processing request: {e}")
        return 1