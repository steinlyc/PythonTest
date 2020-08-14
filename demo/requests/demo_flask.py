from flask import Flask
from flask import request
import json

app = Flask(__name__)


@app.route('/')
def Home():
    data = {'username': 'lyc', 'password': '123456'}
    return json.dumps(data)


@app.route('/login', methods=['GET'])
def Login():
    username = request.args.get('username')
    password = request.args.get('password')
    if username and password:
        data = {'username': username, 'password': password}
        return json.dumps(data)
    else:
        if (not username) and password:
            message = {'message': '请输入用户名'}
            return json.dumps(message)
        elif (not password) and username:
            message = {'message': '请输入密码'}
            return json.dumps(message)
        else:
            message = {'message': '请输入用户名和密码'}
            return json.dumps(message)


@app.route('/content', methods=['POST'])
def Content():
    request_method = request.method
    if request_method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            message = {'username': username, 'password': password}
        else:
            if (not username) and password:
                message = {'message': '请输入用户名'}
            elif (not password) and username:
                message = {'message': '请输入密码'}
            else:
                message = {'message': '请输入用户名和密码'}
    else:
        message = {'message': '请求不合法'}
    return json.dumps(message)


if __name__ == "__main__":
    app.run(debug=True)