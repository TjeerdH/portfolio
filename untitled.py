@app.route("/dice", methods=["POST", "Get"])
def roll_dice():
	if request.method == "POST":
		answer = request.form.to_dict()
		while True:
		    rolling_dice = answer["yn"]
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
			msg3 = random.randrange(1,6)
			msg4 = random.randrange(1,6)
			rolling_dice = answer["yn"]
			if rolling_dice.lower() == "y" or rolling_dice.lower() == "yes":
				   again = True
			else:
				   again = False
				   msg1 = "Thank you for rolling!"
				   break