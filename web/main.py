from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():	
	return 'This is the homepage'

@app.route('/tuna')
def tuna():
	return '<h2>This is tuna</h2>'

@app.route('/bot/<name>')
def bot(name):
	return render_template("profile.html", name=name)

if __name__ == "__main__":
	app.run(debug=True)

