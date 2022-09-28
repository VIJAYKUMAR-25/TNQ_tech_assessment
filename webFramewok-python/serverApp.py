from contextlib import redirect_stderr
from flask import Flask,render_template,redirect,url_for,request

app = Flask(__name__)

@app.route("/calc",methods=['GET','POST'])
def calculator():
    a = int(request.form["a"])
    b = int(request.form["b"])
    operation = request.form.get("operation")
    if(operation == "-"):
        return str(a-b)
    elif(operation == "*"):
        return str(a*b)
    elif(operation == "/"):
        return str(a/b)
    return str(a+b)

@app.route("/")
def home():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run("localhost" ,debug=True)