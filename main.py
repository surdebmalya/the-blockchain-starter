from flask import Flask, render_template, request, redirect, url_for
import requests, os
import send_lead_mail as slm

# Configuration files
app = Flask(__name__)
app.config["DEBUG"] = True

BOOK_NAME = "the-blockchain-starter"
BASE_LINK = "https://book-survey.surdebmalya11.repl.co/" + BOOK_NAME
api_key = os.environ["access_key"]


# Landing page
@app.route('/')
def index():
    return render_template('index.html')

# thank you page
@app.route('/thanks', methods=['POST'])
def thanks():
	return render_template("thanks.html")

# Subscribe1
@app.route('/subscribe1', methods=['POST'])
def subscribe1():
	try:
		email = request.form["email"]
		# store the data on the database
		link = BASE_LINK + '/' + email + '/' + api_key
		res = requests.post(link)
		if res.json()["code"]==200:
			print("STORED IN DATABASE")
			# send the mail
			res = slm.lead_magnet_sending(email)
			if res:
				print("MAIL SENT SUCCESSFULLY")
				return redirect(url_for('thanks'), code=307)
			else:
				return redirect(url_for('index'))
		else:
			return redirect(url_for('index'))
	except:
		return redirect(url_for('index'))

# Subscribe2
@app.route('/subscribe2', methods=['POST'])
def subscribe2():
	try:
		email = request.form["email"]
		# store the data on the database
		link = BASE_LINK + '/' + email + '/' + api_key
		res = requests.post(link)
		if res.json()["code"]==200:
			print("STORED IN DATABASE")
			# send the mail
			res = slm.lead_magnet_sending(email)
			if res:
				print("MAIL SENT SUCCESSFULLY")
				return redirect(url_for('thanks'), code=307)
			else:
				return redirect(url_for('index'))
		else:
			return redirect(url_for('index'))
	except:
		return redirect(url_for('index'))


# Driver code starts from here
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
