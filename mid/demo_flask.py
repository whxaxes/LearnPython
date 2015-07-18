#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    # 直接接文件名，默认目录为templates目录下
    return render_template('test.html')

@app.route('/login', methods=['GET'])
def login():
    return '''
    <form action='/login' method='post'>
        <p><input name="username" type="text"/></p>
        <p><input name="password" type="password"/></p>
        <p><button type="submit">login</button></p>
    </form>
    '''

@app.route('/login', methods=['POST'])
def handle_info():
    if request.form['username']=='admin' and request.form['password']=='123456':
        return '<h1>Hello, Admin</h1>'

    return '<h1>password error</h1>'

app.run()
