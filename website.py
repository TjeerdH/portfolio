from flask import Flask, render_template, send_from_directory, request, redirect, flash
import os
import csv
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import random
import time

app = Flask(__name__)
x = 5

@app.route("/favicon.ico")
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def page(name):
    return render_template(name)

@app.route("/submit_form", methods=["POST", "Get"])
def submit_form():
	if request.method == "POST":
		try:
			data = request.form.to_dict()
			write_csv(data)
			email_confirm(data)
			return redirect("/thankyou.html")
		except:
			return "did not save to database"

	else:
		return "Something went wrong, try again."

@app.route("/guess_game", methods=["POST", "Get"])
def guess_game():

	while True:
	    count = 0
	    if request.method == "POST":
	    	guess = request.form.to_dict()
	    try:
	        if x != int(guess["number"]):
	            if x % 2 == 0:
	                msg = "It is an even number!"
	                count += 1
	                return render_template("/guess.html", msg=msg)
	                break
	            else:
	                msg = "It is an odd number!"
	                count += 1
	                return render_template("/guess.html", msg=msg)
	                break
	        elif x == int(guess["number"]):
	            msg = "Lucky guess! But you are correct!"
	            return render_template("/guess.html", msg=msg)
	            
	    except ValueError:
	        msg = "You don't know what a number is? Only submit numbers between 0 and 100!"
	        count += 1
	        return render_template("/guess.html", msg=msg)
	        continue

	while True:
	    try:
	        guess = request.form.to_dict()
	        if int(guess["number"]) != x:
	            if x < 50:
	                msg = "It is smaller then 50!"
	                count += 1
	                return render_template("/guess.html", msg=msg)
	                break
	            elif x > 50:
	                msg = "It is greater then 50!"
	                return render_template("/guess.html", msg=msg)
	                count += 1
	                break
	        elif x == int(guess["number"]):
	            msg = "You are correct! Not bad on second try!"
	            return render_template("/guess.html", msg=msg)
	            exit()
	    except ValueError:
	        msg = "Really? What about numbers don't you understand? Only submit numbers between 0 and 100!"
	        return render_template("/guess.html", msg=msg)
	        count += 1
	        continue

	while True:
	    try:
	        guess = request.form.to_dict()
	        if int(guess["number"]) != x:
	            if 0 < x < 25:
	                msg = "It is between 0 and 25!"
	                count += 1
	                return render_template("/guess.html", msg=msg)
	                break
	            elif 26 < x < 50:
	                msg = "It is between 26 and 50!"
	                count += 1
	                return render_template("/guess.html", msg=msg)
	                break
	            elif 51 < x < 75:
	                msg = "It is between 51 and 75!"
	                count += 1
	                return render_template("/guess.html", msg=msg)
	                break
	            elif 76 < x < 100:
	                msg = "It is between 76 and 100!"
	                count += 1
	                return render_template("/guess.html", msg=msg)
	                break
	        elif int(guess["number"]) == x:
	            count += 1
	            msg = f"Well done in {count} tries! You are correct!"
	            return render_template("/guess.html", msg=msg)
	            exit()
	    except ValueError:
	        msg = "Come on, You should know how this works by now! Only submit numbers between 0 and 100!"
	        count += 1
	        return render_template("/guess.html", msg=msg)
	        continue

	if int(guess["number"]) != x:
	    while int(guess["number"]) != x:
	        try:
	            guess = request.form.to_dict()
	        except ValueError:
	            msg = "Hey dumdum, Only submit numbers between 0 and 100!"
	            count += 1
	            return render_template("/guess.html", msg=msg)
	            continue
	        if int(guess["number"]) == x:
	            count += 1
	            msg = f"You have guessed correctly! in {count} tries!"
	            return render_template("/guess.html", msg=msg)
	            exit()
	        elif int(guess["number"]) < x:
	            msg = "The answer is higher!"
	            count += 1
	            return render_template("/guess.html", msg=msg)
	            continue
	        elif int(guess["number"]) > x:
	            msg = "The answer is lower!"
	            count += 1
	            return render_template("/guess.html", msg=msg)
	            continue
	elif int(guess["number"]) == x:
	    count += 1
	    msg = f"Well done! in {count} tries!"
	    return render_template("/guess.html", msg=msg)


def write_file(data):
	with open("database.txt", mode="a") as file:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file.write(f"\nName: {name} \nEmail: {email} \nSubject: {subject} \nMessage: {message} \n ")


def write_csv(data):
	with open("database.csv", newline="", mode="a") as database:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([name,email,subject,message])

def email_confirm(data):
	name = data["name"]
	email_address = data["email"]
	subject = data["subject"]
	message = data["message"]
	email_confirmation = EmailMessage()
	email_confirmation["from"] = #Name
	email_confirmation["to"] = email_address
	email_confirmation["bcc"] = pass
	email_confirmation["subject"] = subject
	email_confirmation.set_content(f"Dear Mr/Mrs {name},\nI have received your message:\n \n'{message}'\n \nI will get in touch as soon as I can. \nKind regards,\n\nTjeerd Hoekstra")
	with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.login(#Email, Password)
		smtp.send_message(email_confirmation)

@app.route("/dice", methods=["POST", "Get"])
def dice_roll():
	if request.method == "POST":
		answer = request.form.to_dict()
		while True:
    rolling_dice = answer["answer"]
    if rolling_dice.lower() == "n" or rolling_dice.lower() == "no":
        again = False
        msg1 = "Why did you start the program then....."
        exit()
    elif rolling_dice.lower() == "y" or rolling_dice.lower() == "yes":
        again = True
        break
    else:
        msg1 = "Please enter yes or no!"
        continue


while again:
    msg1 = "Rolling the dice......"
    time.sleep(1.5)
    msg2 = "The value is..."
    time.sleep(0.75)
    msg3 = random.randrange(1,6), end="  "
    msg4 = random.randrange(1,6)
    rolling_dice = answer["answer"]
    if rolling_dice.lower() == "y" or rolling_dice.lower() == "yes":
        again = True
    else:
        again = False
        msg1 = "Thank you for rolling!"
        break



