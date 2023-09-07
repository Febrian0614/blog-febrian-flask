# import aplikasi flask untuk dpakai di web kita
from flask import Flask

#mengatur nama aplikasi
app = Flask(__name__)

#mengatur URI (Universal Resource indentifier),dan apa yang di tampilkan jika URI tersebut di akses
@app.route('/')#ketika alamat http://127.0.0.1:5000/ dipangil, maka server akan mengesekusi fungsi hello()
def hello():#function dengan nama hello
    return 'Hello,World!'

# mengatur URI ke http://127.0.0.1:5000/login,dan mengesekusi fungsi login() jika diakses di alamat URI http://127.0.0.1:5000/login
@app.route("/login")
def login():
    return 'halaman login'
