from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
	return render_template("index.html")

@app.route("/bio")
def page():
	return render_template("bio.html")

@app.route("/my portfolio")
def pro():
	return render_template("projects.html")

@app.route("/pitch")
def pit():
	return render_template("pitch.html")

@app.route("/info")
def info():
	return render_template("contacts.html")

if __name__ =="__main__":

	app.run()