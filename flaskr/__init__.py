# import aplikasi flask,os,flask,jsonify,redirect,dan render_template untuk dipaki di web kita
import os

#impor 50SQL untuk akses database
from cs50 import SQL
#import flash untuk notifikasi pada web
#import jsonify untuk memformat data
#import redirect dan render_template untuk berpindah kehalaman web
# import request dan session untuk mengakses data
from flask import Flask,flash,jsonify,redirect,render_template,request,session

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
