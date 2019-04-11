from flask import Flask, render_template  

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Vicktoria")
def Vicktoria():
    return "Hello, Vicktoria"

if __name__ == "__mainmain__":
    app.run(debug=True)
  