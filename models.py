from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
#create table customer
class Customer(db.Model):
    __tablename__ = "customers"
    customer_id = db.Column(db.Integer,primary_key = True)
    customer_name =db.Column(db.String(30),nullable = False)
    customer_gender = db.Column(db.String(11), nullable =False)
    customer_address = db.Column(db.String(30),nullable =True)
    customer_phone = db.Column(db.String(10),nullable = False,unique = True)
    doctor_id = db.Column(db.Integer,db.ForeignKey('doctors.doctor_id'), nullable=True)
#create table doctor
class Doctor(db.Model):
    __tablename__ = 'doctors'
    doctor_id = db.Column(db.Integer,primary_key = True)
    doctor_name = db.Column(db.String(30),nullable = False)
    doctor_citizen_id = db.Column(db.String(30), nullable =True,unique = True)
    doctor_address = db.Column(db.String(30),nullable =True)
    doctor_phone = db.Column(db.String(30),nullable = True)
    customer = db.relationship("Customer", backref="doctors", lazy=True)
    medicine = db.relationship("Medicine", backref="doctors", lazy=True)
    supplier = db.relationship("Supplier", backref="doctors", lazy=True)
#create table Medicine     
class Medicine(db.Model):
    __tablename__ = 'medicines'
    medicine_id = db.Column(db.Integer,primary_key = True)
    medicine_name = db.Column(db.String(30),nullable = False)
    medicine_effect = db.Column(db.String(100), nullable =True)
    medicine_MFG_date = db.Column(db.DateTime,nullable =False)
    medicine_EXP_date = db.Column(db.DateTime,nullable = False)
    doctor_id = db.Column(db.Integer,db.ForeignKey('doctors.doctor_id'), nullable=True)
#create table supplier
class Supplier(db.Model):
    __tablename__ = 'suppliers'
    supplier_id = db.Column(db.Integer,primary_key = True)
    supplier_name = db.Column(db.String(30),nullable = False)
    supplier_phone= db.Column(db.String(100), nullable =False,unique = True)
    supplier_address = db.Column(db.String(50),nullable =True)
    supplier_email = db.Column(db.String(50),nullable =True)
    doctor_id = db.Column(db.Integer,db.ForeignKey('doctors.doctor_id'), nullable=True)