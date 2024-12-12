from flask import Flask, jsonify
from users import users


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def Home():
    return "Hola Mundo"

@app.route('/users')
def UsersHandler():
    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(debug=True)
