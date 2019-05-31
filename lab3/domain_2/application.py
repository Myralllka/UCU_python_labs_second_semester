import os
import smtplib
import csv
from flask import Flask, render_template, request

# Configure app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    domain = request.form.get("domain")
    if not name or not email or not domain:
        return render_template("failure.html")
    message = """\
              Subject: Domain

              You are registered!"""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    password = open('password.txt').read()
    server.login("armancodebo@gmail.com", password)
    server.sendmail("armancodebo@gmail.com", email, message)
    
    file = open("registrants.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"), request.form.get("domain")))
    file.close()

    return render_template("success.html")


app.run(debug=False, host='0.0.0.0', port=8080)
