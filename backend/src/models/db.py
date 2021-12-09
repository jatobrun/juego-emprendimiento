import os
from sqlalchemy import Column, String, Integer, create_engine, Float
from flask_sqlalchemy import SQLAlchemy
import json
from src import db
from datetime import datetime
from sqlalchemy.sql import func


class Usuarios(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String)
    contraseña = db.Column(db.String)
    correo = db.Column(db.String)
    telefono = db.Column(db.String)
    cedula = db.Column(db.String)
    nombre = db.Column(db.String)
    apellido = db.Column(db.String)
    puntos = db.Column(db.Integer, default = 0)
    fecha_registro = db.Column(db.DateTime(timezone=True), server_default=func.now())
    numero_semana = db.Column(db.String, nullable = False, default =datetime.now().strftime("%W"))
    mes = db.Column(db.String, nullable = False, default =datetime.now().strftime("%m"))
    año = db.Column(db.String, nullable = False, default =datetime.now().strftime("%Y"))

    def format(self):
        return {
                'id': self.id,
                'nombre': self.nombre,
                'correo': self.correo,
                'puntos': self.puntos,
                'fecha': self.fecha_registro.strftime("%m/%d/%Y, %H:%M:%S")
                
        }
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def rollback():
        db.session.rollback()
    
    def __repre__(self):
        return json.dumps(self.format())

class Canje(db.Model):
    __tablename__ = 'canjes'
    id = db.Column(db.Integer, primary_key = True)
    numero_semana = db.Column(db.String, nullable = False, default =datetime.now().strftime("%W"))
    mes = db.Column(db.String, nullable = False, default =datetime.now().strftime("%m"))
    año = db.Column(db.String, nullable = False, default =datetime.now().strftime("%Y"))
    fecha_registro = db.Column(db.DateTime(timezone=True), server_default=func.now())
    nombre_cliente = db.Column(db.String)
    total_puntos = db.Column(db.Float)
    cantidad_total = db.Column(db.Float)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable = False)
    productos = db.relationship('DetalleCanje')
    

    def format(self):
        return {
                'id': self.id,
                'fecha': self.fecha_registro.isoformat(),
                'entrada': self.entrada,
                'total_ecopuntos': self.total_ecopuntos,
                
        }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def rollback():
        db.session.rollback()
    
    def __repre__(self):
        return json.dumps(self.format())

class DetalleCanje(db.Model):
    __tablename__ = "detalle_canje"
    id = db.Column(db.Integer, primary_key = True)
    canje_id = db.Column(db.Integer, db.ForeignKey('canjes.id'))
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
    numero_semana = db.Column(db.String, nullable = False, default =datetime.now().strftime("%W"))
    mes = db.Column(db.String, nullable = False, default =datetime.now().strftime("%m"))
    año = db.Column(db.String, nullable = False, default =datetime.now().strftime("%Y"))
    puntos = db.Column( db.Float)
    cantidad = db.Column(db.Float)
    codigo_id = db.Column(db.Integer, db.ForeignKey('codigos.id'))
    detalle = db.relationship('Producto')
    def format(self):
        return {
                'id': self.id,
                'ecopuntos': self.ecopuntos,
            
        }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def rollback():
        db.session.rollback()
    
    def __repre__(self):
        return json.dumps(self.format())

class Producto(db.Model):
    __tablename__ = 'productos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String, nullable = False)
    detalle = db.Column(db.String)
    codigo = db.Column(db.String)
    foto = db.Column(db.String, nullable = False)
    stock_sin_despachar = db.Column(db.Integer, nullable = False)
    stock_real = db.Column(db.Integer, nullable = False)
    puntos = db.Column(db.Float, nullable = False)

    def format(self):
        return {
                'id': self.id,
                'nombre': self.nombre,
                'ecopuntos': self.ecopuntos,
                'tipo_material_id': self.tipo_producto_id,
                'stock': self.stock_sin_despachar,
                'foto': self.foto.decode('utf-8'),
        }

class Codigos(db.Model):
    __tablename__ = "codigos"
    id = db.Column(db.Integer, primary_key = True)
    token = db.Column(db.String)
    canjeado = db.Column(db.Boolean, default=False, nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable = False)
    descripcion = db.Column(db.String)
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    def rollback():
        db.session.rollback()
    
    def __repre__(self):
        return json.dumps(self.format())