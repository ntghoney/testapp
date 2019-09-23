# -*- coding: utf-8 -*-
"""
@File  : __init__.py.py
@Date  : 2019/9/23/023 15:20
"""
from flask import Flask
from flask import request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route("/login", methods=["POST"])
def login():
    form_data = request.get_json()
    email = form_data["email"]
    password = form_data["password"]
    if email == "admin" and password == "123456":
        return jsonify({
            "code": 1,
            "msg": ""
        })
    return jsonify({
        "code": 0,
        "msg": "用户名或密码错误"
    })


@app.route("/")
def index():
    return render_template("login.html")


@app.errorhandler(404)
def not_found(e):
    return "页面不存在"
