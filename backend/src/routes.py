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

@app.route('/login', methods=['POST'])
def login():
    error = 'd'
    response = {}
    data = request.data
    data_dictionary = json.loads(data)
    try:
        usuario = Usuarios.query.filter(Usuarios.usuario == data_dictionary["usuario"]).first()
        contraseña = data_dictionary['contraseña']
        if usuario.contraseña == contraseña:
            error = False
            response = {
                'succes': True,
                'usuario': usuario.format()
            }
        else:
            error = True
            response = {
                'succes': False,
                'mensaje': "Hubo un error al loguear, intenta de nuevo"
            }
    except:        
        error = True
        print(sys.exc_info())
    
    if error:
        abort(402)
    else:
        return jsonify(response)

@app.route('/registro', methods = ['POST'])
def crear_usuario():
    error = False
    data = request.data
    data_dictionary = json.loads(data)
    cedula = data_dictionary["cedula"]
    nombre = data_dictionary["nombre"]
    apellido = data_dictionary["apellido"]
    correo = data_dictionary["correo"]
    telefono = data_dictionary["telefono"]
    usuario = data_dictionary["usuario"]
    contraseña = data_dictionary["contraseña"]
    if Usuarios.query.filter(Usuarios.usuario == usuario).first():
        return jsonify({
                        'success': False,
                        'mensaje': "Este nombre de usuario ya está en uso"
                        })
    elif Usuarios.query.filter(Usuarios.cedula == cedula).first():
        return jsonify({
                        'success': False,
                        'mensaje': "Esta cedula ya existe"
                        })
    elif Usuarios.query.filter(Usuarios.correo == correo).first():
        return jsonify({
                        'success': False,
                        'mensaje': "Este correo ya está registrado"
                        })
    else:
        try: 
            usuario = Usuario(usuario = usuario, contraseña = contraseña, \
                               cedula = cedula, nombre = nombre, apellido = apellido, \
                               correo = correo, telefono = telefono )
            usuario.insert()
        except:
            error = True
            Usuarios.rollback()
            print(sys.exc_info())
    if error:
        abort(422)
    else:
        #enviar_email(correo = ecoAmigo.correo)
        return jsonify({
                        'success': True,
                        'mensaje': "Usuario creado satisfactoriamente"
                        })

@app.route('/crear-canje', methods = ['POST'])
def crear_canje():
    error = False
    data = request.data
    data_dictionary = json.loads(data)
    usuario_id = data_dictionary['usuario_id']
    total_puntos = data_dictionary['total_puntos']
    cantidad_total = data_dictionary['cantidad_total']
    producto_id = data_dictionary['producto_id']    
    usuario = Usuarios.query.filter(Usuarios.id == usuario_id).first()
    producto = Producto.query.filter(Producto.id == producto_id).first()
    detalles = []
    if total_puntos > usuario.puntos:
            return jsonify({
                            'success': False,
                            'mensaje': "Insuficiencia de puntos"
                            })
    elif producto.stock_sin_despachar < cantidad_total:
        return jsonify({
                            'success': False,
                            'mensaje': "Insuficiencia de stock"
                            })
    else:
        try: 
            producto.stock_sin_despachar -= cantidad_total
            producto.update()
            canje = Canje(total_puntos = total_puntos, cantidad_total = cantidad_total, \
                            usuario_id = usuario_id, \
                            nombre_cliente = f"{usuario.nombre} {usuario.apellido}", \
                            producto_id = producto_id)
            canje.insert()
            usuario.puntos -= total_puntos
            usuario.update()
        except:
            error = True
            Canje.rollback()
            print(sys.exc_info())
        try:
            token = secrets.token_hex(4)
            codigo = Codigos(token = token, usuario_id = usuario_id)
            codigo.insert()
        except:
            error = True
            Codigos.rollback()
            canje.delete()
            print(sys.exc_info())   

    if error:
        abort(422)
    else:
        #enviar_email(correo = usuario.correo, token = codigo.token)
        return jsonify({
                        'success': True,
                        'token': codigo.token
                        })
@app.route('/productos')
def get_productos():
    error = False
    productos = Producto.query.all()
    response = [producto.format() for producto in productos if producto.stock_sin_despachar > 0]
    if len(response) > 0:
        return jsonify({
                            'success': True,
                            'premios': response
                            })
    else:
        return jsonify({
                            'success': False,
                            'mensaje': "No Hay premios"
                            })
@app.route('/game-over', methods = ['POST'])
def game_over():
    error = False
    data = request.data
    data_dictionary = json.loads(data)
    usuario_id = data_dictionary["usuario_id"]
    puntos = data_dictionary["puntos"]

    try: 
        usuario = Usuarios.query.filter(Usuarios.id == usuario_id).first()
        usuario.puntos += puntos 

        usuario.update
    
    except:
        error = True
        Usuarios.rollback()
        print(sys.exc_info())   

    if error:
        abort(404)
    else:
        return jsonify({
                        'success': True,
                        'mensaje': "puntos acreditados exitosamente"
        })