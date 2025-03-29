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
    

def issueBooks(sid, isbn):
    val1 = os.environ['dbUser']
    val2 = os.environ['dbPwd']
    flag = -1
    try:
        db=mc.connect(host="localhost",user=val1,password=val2)
        if (db.is_connected()):
            print('DATABASE CONNECTED SUCCESSFULLY')
            cursor=db.cursor()
            cursor.execute("use lj;")
            query = "select b1, b2, b3, b4, b5 from students where sid='{}';".format(sid)
            cursor.execute(query)
            borrows = cursor.fetchall()
            print(borrows)

            for i in range(5):
                if borrows[0][i] == None:
                    flag = i
                    print(i)
                    query = "update students set b{}='{}' where sid='{}';".format(i+1, isbn ,sid)
                    cursor.execute(query)
                    break
            if flag == -1:
                print("no space")
            db.commit()
            db.close()
            print(f"Done")
            return flag
        else:
            return 1
    except Exception as e:
        print(f"Error processing request: {e}")
        return 1
    
def addMember(sid):
    val1 = os.environ['dbUser']
    val2 = os.environ['dbPwd']
    flag = 0
    try:
        db=mc.connect(host="localhost",user=val1,password=val2)
        if (db.is_connected()):
            print('DATABASE CONNECTED SUCCESSFULLY')
            cursor=db.cursor()
            cursor.execute("use lj;")
            query = "insert into students (uname) values ('{}');".format(sid)
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