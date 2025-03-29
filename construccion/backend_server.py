# backend_server.py
from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
SECRET_KEY = 'tu_clave_secreta' 

def authenticate_token():
    token = None
    if 'Authorization' in request.headers:
        token = request.headers['Authorization'].split(" ")[1]
    
    if not token:
        return jsonify({'message': 'Token es necesario'}), 400 

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return data
    except jwt.ExpiredSignatureError:
        return jsonify({'message': 'Token ha expirado'}), 403
    except jwt.InvalidTokenError:
        return jsonify({'message': 'Token inválido'}), 403 

@app.route('/protected', methods=['GET'])
def protected():
    user_data = authenticate_token()
    if isinstance(user_data, tuple):  
        return user_data

    return jsonify({'message': f'Hola {user_data["username"]}, tienes acceso a este endpoint.'})

if __name__ == '__main__':
    app.run(port=4000)
