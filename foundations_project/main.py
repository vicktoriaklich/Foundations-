#import Flask
from flask import Flask, render_template

#__name__ meins current file which will be representing my web application
app = Flask(__name__)

#default page -> need to insert name of webpage before slash
@app.route("/")

#function will be activated after the user goes to the page
def home():
    return "Welcome to Foundations!"

#if you add "/Vicktoria" after localhost:5000 it will display this: 
@app.route("/Vicktoria")
def Vicktoria():
	return "Welcome, Vicktoria!"

"""when I run my python script, Python assigns the name "__main__" to the script 
when executed
If I import another script, the if statement will prevent other scripts from running. 
When I run main.py, it will change its name to __main__ and only then will that if 
statement activate"""

""" app.run(debug=True) runs the application. The True statement allows possible Python
errors to appear on the web page (for tracing errors)"""

if __name__ == "__main__":
   app.run(debug=True)