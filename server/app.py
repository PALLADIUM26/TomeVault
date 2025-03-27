from flask import Flask, request, jsonify
import os
import random
from flask_cors import CORS
import appAuth
import appAdmin
import appLibra
import appStud


app = Flask(__name__)
CORS(app)


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password1 = data.get('password1')
        og_otp = str(data.get('og_otp'))
        category = data.get('category')
        print(f"Received") #print to the console for debugging.
        appAuth.sendmail(email, og_otp)
        appAuth.save1(username, email, password1, category)
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
        appAuth.save2(email)
        return jsonify({'message': 'Data received'})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': str(e), 'message':'An error occurred on the server.'}), 500 #return an error code and message.


@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username')
        password1 = data.get('password1')
        t = appAuth.search(username, password1)
        print(t)
        # return jsonify({'message': 'Signed In'})
        return jsonify({'message': t})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': str(e), 'message':'An error occurred on the server.'}), 500 #return an error code and message.


@app.route('/showBooks', methods=['POST'])
def showBooks():
    try:
        appAdmin.showBookDetails()
        return jsonify({'message': 'Showing'})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': str(e), 'message':'An error occurred on the server.'}), 500 #return an error code and message.


@app.route('/viewUsers', methods=['POST'])
def viewUsers():
    try:
        data = appAdmin.viewUserDetails()
        return jsonify({'message': data})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': str(e), 'message':'An error occurred on the server.'}), 500 #return an error code and message.


@app.route('/searchBooks', methods=['POST'])
def searchBooks():
    try:
        data = request.get_json()
        # username = data.get('username')
        bookKey = data.get('bookKey')
        data2 = appLibra.searchBooks(bookKey)
        return jsonify({'message': data2})
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({'error': str(e), 'message':'An error occurred on the server.'}), 500


if __name__ == '__main__':
    app.run(debug=True)

