from flask import Flask, request, abort, jsonify, send_file
import json
import sys
from src import app
from src.models.db import *
from sqlalchemy import and_, func, desc
from datetime import datetime
import base64
import math
import operator
import secrets

@app.after_request
def after_request(response):
    
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

@app.route('/')
def index():
    print("Hola")
    return jsonify({
        "hola":"Mundo"
    })
