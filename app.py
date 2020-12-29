from flask import Flask, render_template, request, redirect, url_for
import http.client
import json
from random import randint

app = Flask(__name__)

# app settings
app.secret_key = ''

# server credentials
HOST = "127.0.0.1"
PORT = 5000
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
CAPCHA = ''

@app.route('/')
def index():
    CAPCHA = ''
    for _ in range(5):
        index = randint(0, 25)
        CAPCHA += ALPHABET[index]

    return render_template('index.html', capcha=CAPCHA)

@app.route('/lead', methods=['POST'])
def add_lead():
    name = request.form['name']
    id_number = request.form['id_number']
    email = request.form['email']
    mobile = request.form['mobile']
    capcha = request.form['capcha']

    connection = http.client.HTTPConnection(HOST, PORT)
    data = {
        "name": name,
        "id_number": id_number,
        "email": email,
        "mobile": mobile
    }
    payload = json.dumps(data)
    headers = {
    'Content-Type': 'application/json'
    }
    connection.request("POST", "/lead", payload, headers)
    response = connection.getresponse()
    data = response.read()

    return redirect(url_for('congratulation'))

@app.route('/congratulation')
def congratulation():
    return render_template('congratulation.html')

if __name__ == '__main__':
    app.run(host='192.168.10.242', port=3000, debug=True)