from flask import Flask, request, jsonify
import os
import random
# from pythonScripts import predict
from flask_cors import CORS
import mysql.connector as mc
import smtplib

app = Flask(__name__)
CORS(app)

'''
def sendmail(mail, otp):
    sub='SIGNUP VERIFICATION'
    msg="LOL JOB WORLD\nOTP:"+otp+"\nDO NOT SHARE THIS."
    try:
        server=smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login("your email","your app password")
        message='Subject: {}\n\n{}'.format(sub,msg)
        server.sendmail(mail,mail,message)
        server.quit()
        print('EMAIL SENT SUCCESSFULLY!')
        return otp
    except:
        print('SOMETHING WENT WRONG!')
'''
def sendmail(mail, otp):
    print("mail sent")

def save1(username, email, password1):
    try:
        db=mc.connect(host="localhost",user="user",password="your password")
        if (db.is_connected()):
            print('DATABASE CONNECTED SUCCESSFULLY')
            cursor=db.cursor()
            cursor.execute("use lj;")
            query="insert into tempData (uname,mail,pwd) values ('{}','{}','{}')".format(username,email,password1)
            cursor.execute(query)
            db.commit()
            db.close()
            print(f"Stored")
    except Exception as e:
        print(f"Error processing request: {e}")

def save2(email):
    try:
        db=mc.connect(host="localhost",user="user",password="password")
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
            
            x = 'x'
            query="insert into data (uname,mail,pwd,type) values ('{}','{}','{}','{}')".format(b[0],b[1],b[2],x)
            cursor.execute(query)
            cursor.execute("delete from tempData where email='{}'".format(email))
            db.commit()
            db.close()
            print(f"Stored2")
    except Exception as e:
        print(f"Error processing request: {e}")


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        og_otp = str(data.get('og_otp'))
        print(f"Received") #print to the console for debugging.
        sendmail(email, og_otp)
        save1(username, email, password1)
        print("Received2")
        return jsonify({'message': 'Data received'})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': str(e), 'message':'An error occurred on the server.'}), 500 #return an error code and message.


@app.route('/verify', methods=['POST'])
def verify():
    try:
        data = request.get_json()
        email = data.get('email')
        save2(email)
        return jsonify({'message': 'Data received'})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': str(e), 'message':'An error occurred on the server.'}), 500 #return an error code and message.


if __name__ == '__main__':
    app.run(debug=True)

