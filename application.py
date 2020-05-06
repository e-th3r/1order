from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") 
def index():
	return render_template("index.html")
@app.route("/index.html")
def index1():
	return render_template("index.html")
@app.route("/whatis.html")
def whatis():
	return render_template("whatis.html")
@app.route("/aboutproject.html")
def aboutproject():
	return render_template("aboutproject.html")
if __name__ == '__name__':
    app.run()