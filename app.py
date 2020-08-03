from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import users

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///lautanas"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Front page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        print("Tulee postiin")
        username = request.form["username"]
        password = request.form["password"]
        name = request.form["name"]
        level = int(request.form["level"])
        print("Arvot tallentuvat")
        if users.register(username,password,name,level,db):
            return redirect("/")
        else:
            return render_template("error.html", message = "Virhe käyttäjän luonnissa.")

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if users.login(username,password, db):
            return redirect("/")
        else:
            return render_template("error.html", message = "Väärä käyttäjätunnus tai salasana.")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/purchase")
def purchase():
    return render_template("purchase.html")

#if __name__ == "__main__":
#    app.run(debug=True)
