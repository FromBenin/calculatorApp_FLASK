from flask import Flask, render_template, request, flash

app: Flask = Flask(__name__)
app.secret_key = "Bigman-1234"

@app.route("/")
def index() -> str:    
    flash("What's your name?")
    return render_template("index.html")

@app.route("/age", methods=["POST", "GET"])
def age() -> str:    
    flash("Hi " + str(request.form['name_input']) + ". Please enter your year of birth")
    return render_template("age.html")  

@app.route("/add", methods=["POST", "GET"])
def add() -> str:
    agevalue: int= 2022 - int(request.form['num1_input'])
    flash("You were born in the year " +  str(request.form['num1_input']) + " and your are " + str(agevalue) + "yrs old. Add two numbers")
    return render_template("add.html")

@app.route("/subtract", methods=["POST", "GET"])
def subtract() -> str:
    totalvalue: int= int(request.form['num1_input']) + int(request.form['num2_input'])
    flash("The total SUM of " + str(request.form['num1_input'])+" and " + str(request.form['num2_input']) + " is " + str(totalvalue) + ". Subtract two numbers")
    return render_template("subtract.html")

@app.route("/multiply", methods=["POST", "GET"])
def multiply() -> str:
    totalvalue: int= int(request.form['num1_input']) - int(request.form['num2_input'])
    flash("The difference betweeen " + str(request.form['num1_input']) + " and " + str(request.form['num2_input']) + " is " + str(totalvalue) + ". Multiply two numbers")
    return render_template("multiply.html")


@app.route("/thanks", methods=["POST", "GET"])
def thanks() -> str:
    totalvalue: int= int(request.form['num1_input']) * int(request.form['num2_input'])
    flash("The product of " + str(request.form['num1_input']) + " and " + str(request.form['num2_input']) + " is " + str(totalvalue) + ". THANK YOU!")
    return render_template("thanks.html")