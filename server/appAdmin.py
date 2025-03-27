import mysql.connector as mc
import os

def showBookDetails():
    val1 = os.environ['dbUser']
    val2 = os.environ['dbPwd']
    try:
        db=mc.connect(host="localhost",user=val1,password=val2)
        if (db.is_connected()):
            print('DATABASE CONNECTED SUCCESSFULLY')
            cursor=db.cursor()
            cursor.execute("use lj;")
            query = "select * from books;"
            cursor.execute(query)
            bookDetails = cursor.fetchall()
            print(bookDetails)
            db.commit()
            db.close()
            print(f"Shown")
            return bookDetails
    except Exception as e:
        print(f"Error processing request: {e}")


def viewUserDetails():
    val1 = os.environ['dbUser']
    val2 = os.environ['dbPwd']
    try:
        db=mc.connect(host="localhost",user=val1,password=val2)
        if (db.is_connected()):
            print('DATABASE CONNECTED SUCCESSFULLY')
            cursor=db.cursor()
            cursor.execute("use lj;")
            query = "select * from data;"
            cursor.execute(query)
            userDetails = cursor.fetchall()
            # print(userDetails)
            db.commit()
            db.close()
            print(f"Shown")
            return userDetails
        else:
            return 1
    except Exception as e:
        print(f"Error processing request: {e}")
        return 1