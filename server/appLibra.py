import mysql.connector as mc
import os

def searchBooks(bookKey):
    val1 = os.environ['dbUser']
    val2 = os.environ['dbPwd']
    try:
        db=mc.connect(host="localhost",user=val1,password=val2)
        if (db.is_connected()):
            print('DATABASE CONNECTED SUCCESSFULLY')
            cursor=db.cursor()
            cursor.execute("use lj;")
            query = "select * from books where bookname='{}' or author='{}';".format(bookKey,bookKey)
            cursor.execute(query)
            bookDetails = cursor.fetchall()
            db.commit()
            db.close()
            print(f"Shown")
            print(bookDetails)
            return bookDetails
        else:
            return 1
    except Exception as e:
        print(f"Error processing request: {e}")
        return 1