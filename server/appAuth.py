import smtplib
import mysql.connector as mc
import os

def sendmail2(mail, otp):
    val1 = os.environ['email_sender']
    val2 = os.environ['appPassword']
    sub='SIGNUP VERIFICATION'
    msg="LOL JOB WORLD\nOTP:"+otp+"\nDO NOT SHARE THIS."
    try:
        server=smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(val1,val2)
        message='Subject: {}\n\n{}'.format(sub,msg)
        server.sendmail(mail,mail,message)
        server.quit()
        print('EMAIL SENT SUCCESSFULLY!')
        return otp
    except:
        print('SOMETHING WENT WRONG!')



def sendmail(mail, otp):
    print("mail sent")

def save1(username, email, password1, category):
    val1 = os.environ['dbUser']
    val2 = os.environ['dbPwd']
    try:
        db=mc.connect(host="localhost",user=val1,password=val2)
        if (db.is_connected()):
            print('DATABASE CONNECTED SUCCESSFULLY')
            cursor=db.cursor()
            cursor.execute("use lj;")
            query="insert into tempData (uname,mail,pwd,category) values ('{}','{}','{}','{}')".format(username,email,password1,category)
            cursor.execute(query)
            db.commit()
            db.close()
            print(f"Stored")
    except Exception as e:
        print(f"Error processing request: {e}")

def save2(email):
    val1 = os.environ['dbUser']
    val2 = os.environ['dbPwd']
    try:
        db=mc.connect(host="localhost",user=val1,password=val2)
        if (db.is_connected()):
            print('DATABASE CONNECTED SUCCESSFULLY')
            cursor=db.cursor()
            cursor.execute("use lj;")
            query="select * from tempData where mail='{}';".format(email)
            cursor.execute(query)
            a=cursor.fetchall()
            b = []
            for i in a:
                for j in i:
                    b.append(j)
            query="insert into data (uname,mail,pwd,type) values ('{}','{}','{}','{}')".format(b[0],b[1],b[2],b[3])
            cursor.execute(query)
            cursor.execute("delete from tempData where mail='{}'".format(email))
            db.commit()
            db.close()
            print(f"Stored2")
    except Exception as e:
        print(f"Error processing request: {e}")

def search(username, password1):
    val1 = os.environ['dbUser']
    val2 = os.environ['dbPwd']
    try:
        db=mc.connect(host="localhost",user=val1,password=val2)
        flag = 0
        if (db.is_connected()):
            print('DATABASE CONNECTED SUCCESSFULLY')
            cursor=db.cursor()
            cursor.execute("use lj;")
            query="select pwd,type from data where uname='{}';".format(username)
            cursor.execute(query)
            a = cursor.fetchall()
            b = a[0][0]
            c = a[0][1]
            if b == password1:
                flag = 1
            db.commit()
            db.close()
            if flag == 1:
                print(f"Found")
                return c
            else:
                return flag
    except Exception as e:
        print(f"Error processing request: {e}")
        return (f"Error processing request: {e}")
