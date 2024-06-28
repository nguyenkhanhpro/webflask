from flask import Flask, render_template, request
from models import *

app = Flask(__name__, template_folder="templates") 
app.config["SECRET_KEY"] ="khanh" #encode session
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/website" #this is localhost mysql
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#Home
@app.route("/home")
def home():
    return render_template("home.html") 

#Table customer
@app.route("/customer")
def customer():
    return render_template("customer.html") 

@app.route("/add_customer")
def add_customer():
    return render_template("add_customer.html")

@app.route('/insert_customer')
def insert_customer():
    customer_name = request.args.get('customer_name') #request.args.get(“variable”) is used to received data
    customer_gender = request.args.get('customer_gender')
    customer_address = request.args.get('customer_address')
    customer_phone = request.args.get('customer_phone')
    doctor_id = request.args.get('doctor_id')
    customer = Customer(customer_name=customer_name, customer_gender=customer_gender, 
                        customer_address=customer_address,customer_phone=customer_phone,
                        doctor_id=doctor_id)
    db.session.add(customer) #db.session.add is used to add value
    db.session.commit()
    return render_template("add_customer_successfull.html")

@app.route("/info_customer")
def infor_customer():
    customers = Customer.query.all() #query.all() is used to query about all data 
    return render_template("infor_customer.html", customers=customers)

@app.route("/update_customer")
def update_customer():
    customer_id = request.args.get("customer_id")
    customer = Customer.query.get(customer_id) #query.all() is used to query for one value
    return render_template("update_customer.html", customer=customer)

@app.route('/update_customer_commit')
def update_customer_commit():
    customer_id = request.args.get('customer_id')
    customer = Customer.query.get(customer_id)
    customer.customer_name = request.args.get('customer_name')
    customer.customer_gender = request.args.get('customer_gender')
    customer.customer_address = request.args.get('customer_address')
    customer.customer_phone = request.args.get('customer_phone')
    customer.doctor_id = request.args.get('doctor_id')
    db.session.commit()
    return render_template("update_customer_successfull.html")

@app.route("/delete_customer")
def delete_customer():
    customer_id = request.args.get("customer_id")
    customer = Customer.query.get(customer_id)
    db.session.delete(customer) #db.session.delete is used to delete value
    db.session.commit()
    return render_template("delete_customer.html", customer=customer)

#Table doctor
@app.route("/doctor")
def doctor():
    return render_template("doctor.html")

@app.route("/add_doctor")
def add_doctor():
    return render_template("add_doctor.html")

@app.route('/insert_doctor')
def insert_doctor():
    doctor_name = request.args.get('doctor_name')
    doctor_citizen_id = request.args.get('doctor_citizen_id')
    doctor_address = request.args.get('doctor_address')
    doctor_phone = request.args.get('doctor_phone')
    doctor = Doctor(doctor_name=doctor_name, doctor_citizen_id=doctor_citizen_id, doctor_address=doctor_address,doctor_phone=doctor_phone)
    db.session.add(doctor)
    db.session.commit()
    return render_template("add_doctor_successfull.html")

@app.route("/info_doctor")
def infor_doctor():
    doctors = Doctor.query.all()
    return render_template("infor_doctor.html", doctors=doctors)

@app.route("/update_doctor")
def update_doctor():
    doctor_id = request.args.get("doctor_id")
    doctor = Doctor.query.get(doctor_id)
    return render_template("update_doctor.html", doctor=doctor)

@app.route('/update_doctor_commit')
def update_doctor_commit():
    doctor_id = request.args.get('doctor_id')
    doctor = Doctor.query.get(doctor_id)
    doctor.doctor_name = request.args.get('doctor_name')
    doctor.doctor_citizen_id = request.args.get('doctor_citizen_id')
    doctor.doctor_address = request.args.get('doctor_address')
    doctor.doctor_phone = request.args.get('doctor_phone')
    db.session.commit()
    return render_template("update_doctor_successfull.html")

@app.route("/delete_doctor")
def delete_doctor():
    doctor_id = request.args.get("doctor_id")
    doctor = Doctor.query.get(doctor_id)
    db.session.delete(doctor)
    db.session.commit()
    return render_template("delete_doctor.html", doctor=doctor)

#Table medicine
@app.route("/medicine")
def medicine():
    return render_template("medicine.html")

@app.route("/add_medicine")
def add_medicine():
    return render_template("add_medicine.html")

@app.route('/insert_medicine')
def insert_medicine():
    medicine_name = request.args.get('medicine_name')
    medicine_effect = request.args.get('medicine_effect')
    medicine_MFG_date = request.args.get('medicine_MFG_date')
    medicine_EXP_date = request.args.get('medicine_EXP_date')
    doctor_id = request.args.get('doctor_id')
    medicine = Medicine(medicine_name=medicine_name, medicine_effect=medicine_effect, medicine_MFG_date=medicine_MFG_date,medicine_EXP_date=medicine_EXP_date,doctor_id=doctor_id)
    db.session.add(medicine)
    db.session.commit()
    return render_template("add_medicine_successfull.html")

@app.route("/infor_medicine")
def infor_medicine():
    medicines = Medicine.query.all()
    return render_template("infor_medicine.html", medicines=medicines)

@app.route("/update_medicine")
def update_medicine():
    medicine_id = request.args.get("medicine_id")
    medicine = Medicine.query.get(medicine_id)
    return render_template("update_medicine.html", medicine=medicine)

@app.route('/update_medicine_commit')
def update_medicine_commit():
    medicine_id = request.args.get('medicine_id')
    medicine = Medicine.query.get(medicine_id)
    medicine.medicine_name = request.args.get('medicine_name')
    medicine.medicine_effect = request.args.get('medicine_effect')
    medicine.medicine_MFG_date = request.args.get('medicine_MFG_date')
    medicine.medicine_EXP_date = request.args.get('medicine_EXP_date')
    medicine.doctor_id = request.args.get('doctor_id')
    db.session.commit()
    return render_template("update_medicine_successfull.html")

@app.route("/delete_medicine")
def delete_medicine():
    medicine_id = request.args.get("medicine_id")
    medicine = Medicine.query.get(medicine_id)
    db.session.delete(medicine)
    db.session.commit()
    return render_template("delete_medicine.html", medicine=medicine)

# Table supplier
@app.route("/supplier")
def supplier():
    return render_template("supplier.html")

@app.route("/add_supplier")
def add_supplier():
    return render_template("add_supplier.html")

@app.route('/insert_supplier')
def insert_supplier():
    supplier_name = request.args.get('supplier_name')
    supplier_phone = request.args.get('supplier_phone')
    supplier_address = request.args.get('supplier_address')
    supplier_email = request.args.get('supplier_email')
    doctor_id = request.args.get('doctor_id')
    supplier = Supplier(supplier_name=supplier_name, supplier_phone=supplier_phone, supplier_address=supplier_address,supplier_email=supplier_email,doctor_id=doctor_id)
    db.session.add(supplier)
    db.session.commit()
    return render_template("add_supplier_successfull.html")

@app.route("/info_supplier")
def infor_supplier():
    suppliers = Supplier.query.all()
    return render_template("infor_supplier.html", suppliers=suppliers)

@app.route("/update_supplier")
def update_supplier():
    supplier_id = request.args.get("supplier_id")
    supplier = Supplier.query.get(supplier_id)
    return render_template("update_supplier.html", supplier=supplier)

@app.route('/update_supplier_commit')
def update_supplier_commit():
    supplier_id = request.args.get('supplier_id')
    supplier = Supplier.query.get(supplier_id)
    supplier.supplier_name = request.args.get('supplier_name')
    supplier.supplier_phone = request.args.get('supplier_phone')
    supplier.supplier_address = request.args.get('supplier_address')
    supplier.supplier_email = request.args.get('supplier_email')
    supplier.doctor_id = request.args.get('doctor_id')
    db.session.commit()
    return render_template("update_supplier_successfull.html")

@app.route("/delete_supplier")
def delete_supplier():
    supplier_id = request.args.get("supplier_id")
    supplier = Supplier.query.get(supplier_id)
    db.session.delete(supplier)
    db.session.commit()
    return render_template("delete_supplier.html", supplier=supplier)

#Find information
@app.route("/find_information")
def find_information():
    return render_template("find_all.html")

@app.route("/showAll")
def showAll():
    doctor_id = request.args.get('doctor_id')
    doctors = Doctor.query.get(doctor_id)
    customers = doctors.customer
    medicines= doctors.medicine
    suppliers = doctors.supplier 
    return render_template("show_all.html", doctors =doctors, customers=customers,medicines = medicines,suppliers=suppliers)

if __name__ == '__main__':
    app.run(debug=True)