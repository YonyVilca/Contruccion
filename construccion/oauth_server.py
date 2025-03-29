# oauth_server.py
from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = 'tu_clave_secreta'  

@app.route('/token', methods=['POST'])
def token():
    username = request.json.get('username')
    token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, SECRET_KEY, algorithm='HS256')
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(port=3000)
