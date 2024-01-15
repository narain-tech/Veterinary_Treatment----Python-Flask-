import os
import random
from datetime import date
import re

from urllib import request
import pymysql
import ar_master
import smtplib, ssl
from flask import Flask, render_template, flash, request, session, current_app, send_from_directory
from werkzeug.utils import redirect, secure_filename



# ps = PorterStemmer()
app = Flask(__name__, static_folder="static")
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
user='root'
password=''
host='localhost'
database='python_Veterinary_treatment'
mm = ar_master.master_flask_code()
################################################################### HOME
@app.route("/")
def homepage():
    return render_template('index.html')
@app.route("/admin")
def admin():
    return render_template('admin.html')
@app.route("/admin_login", methods = ['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['pass'] == 'admin':
            return render_template('admin_home.html', flashMessage = True, data = "Login Successfully")
        else:
            print("else")
            return render_template('admin.html', flashMessage = True, error='Incorrect Username or Password',data = "Failed")
@app.route("/admin_home")
def admin_home():
    return render_template('admin_home.html')


@app.route("/patient_home")
def patient_home():
    return render_template('patient_home.html')

@app.route("/patient_appointment", methods=['GET', 'POST'])
def patient_appointment():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email_id = request.form['email_id']
        phone_num = request.form['phone_num']
        species = request.form['species']
        pet_name = request.form['pet_name']
        reason = request.form['reason']
        date = request.form['date']
        time = request.form['time']
        maxin = mm.find_max_id("patient_appointment_details")
        qq = "insert into patient_appointment_details values('" + str(maxin) + "','" + str(full_name) + "','" + str(email_id) + "','" + str(phone_num
            ) + "','" + str(pet_name) + "','" + str(species) + "','" + str(reason) + "','" + str(date) + "','" + str(time) + "','0','0')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('patient_appointment.html', flashMessage=True, data="Booked Successfully")
    return render_template('patient_appointment.html')


@app.route("/patient_patient", methods=['GET', 'POST'])
def patient_patient():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        age = request.form['age']
        email = request.form['email']
        address = request.form['address']

        maxin = mm.find_max_id("patient_profile")
        qq = "insert into patient_profile values('" + str(maxin) + "','" + str(name) + "','" + str(phone) + "','" + str(
            age) + "','" + str(email) + "','" + str(address) + "','0','0')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('patient_patient.html', flashMessage=True, data="Successfully")
    return render_template('patient_patient.html')



############################################################################################################
@app.route("/patient_register", methods=['GET', 'POST'])
def patient_register():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']


        maxin = mm.find_max_id("patient_details")
        qq = "insert into patient_details values('" + str(maxin) + "','" + str(name) + "','" + str(contact) + "','" + str(
            email) + "','" + str(address) + "','" + str(username) + "','" + str(password) + "','0','0')"
        result = mm.insert_query(qq)

        if (result == 1):
            return render_template('patient.html', flashMessage=True, data="Successfully")

    return render_template('patient_register.html')

@app.route("/patient",methods = ['GET', 'POST'])
def patient():
    msg=''
    if request.method == 'POST':
        n = request.form['uname']
        g = request.form['pass']
        n1=str(n)
        g1=str(g)

        q=("SELECT * from patient_details where email='" + str(n1) + "' and password='" + str(g) + "'")
        data=mm.select_direct_query(q)
        data=len(data)
        if data==0:

            return render_template('patient.html',flashMessage=True,data="Failed",error='Incorrect Username or Password')
        else:
            msg='Success'
            session['user'] =n
            return render_template('patient_home.html',sid=n,flashMessage=True,data="Login Successfully")
    return render_template('patient.html',error=msg)


@app.route("/admin_view_booking",methods = ['GET', 'POST'])
def admin_view_booking():
    data = mm.select_direct_query("select * from patient_appointment_details")
    return render_template('admin_view_booking.html', items=data)

@app.route("/admin_view_delete/<id>",methods = ['GET', 'POST'])
def admin_view_delete(id):
    data=mm.insert_query("delete from patient_appointment_details where id='"+str(id)+"'")
    print(data)
    return admin_view_booking()


@app.route("/admin_view_edit/<id>",methods = ['GET', 'POST'])
def admin_view_edit(id):
    session["id"]=id
    data=mm.select_direct_query("select * from patient_appointment_details where id='"+id+"'")
    print(data)
    return render_template('admin_view_edit.html', items=data[0])


@app.route("/admin_view_edit_1", methods=['GET', 'POST'])
def admin_view_edit_1():
    id=session["id"]
    if request.method == 'POST':
        full_name = request.form['full_name']
        email_id = request.form['email_id']
        phone_num = request.form['phone_num']
        species = request.form['species']
        pet_name = request.form['pet_name']
        reason = request.form['reason']
        date = request.form['date']
        time = request.form['time']
        qq="update patient_appointment_details set full_name='"+str(full_name)+"',email_id='"+str(email_id)+"',phone_num='"+str(phone_num)+"',species='"+str(species)+"',pet_name='"+str(pet_name)+"',reason='"+str(reason)+"',date='"+str(date)+"',time='"+str(time)+"' where id='"+str(id)+"'"
        print(qq)
        result = mm.insert_query(qq)
       

        if (result == 1):
            return admin_view_booking()

    return render_template('patient_register.html')



@app.route("/admin_view_patient",methods = ['GET', 'POST'])
def admin_view_patient():
    data = mm.select_direct_query("select * from patient_details")
    return render_template('admin_view_patient.html', items=data)
@app.route("/admin_view_edit2/<id>",methods = ['GET', 'POST'])
def admin_view_edit2(id):
    session["id"]=id
    data=mm.select_direct_query("select * from patient_details where id='"+id+"'")
    print(data)
    return render_template('patient_register.html', items=data[0])



@app.route("/admin_view_edit_3", methods=['GET', 'POST'])
def admin_view_edit_3():
    id=session["id"]
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']

        qq="update patient_details set name='"+str(name)+"',contact='"+str(contact)+"',email='"+str(email)+"',address='"+str(address)+"',username='"+str(username)+"',password='"+str(password)+"' , where id='"+str(id)+"'"
        print(qq)
        result = mm.insert_query(qq)

        if (result == 1):
            return admin_view_patient()

    return render_template('admin_home.html')
@app.route("/admin_view_delete1/<id>",methods = ['GET', 'POST'])
def admin_view_delete1(id):
    data=mm.insert_query("delete from patient_details where id='"+str(id)+"'")
    print(data)
    return admin_view_patient()

@app.route("/about",methods = ['GET', 'POST'])
def about():
    return render_template('about us.html')


@app.route("/contact",methods = ['GET', 'POST'])
def contact():
    return render_template('contact us.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
