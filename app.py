from flask import Flask
from flask import redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import users, lessons

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

@app.route("/listlessons")
def ls_lessons():
    tunnit = lessons.get_list(db)
    return render_template("list_lessons.html", lessons=tunnit)

@app.route("/lessons", methods=["get","post"])
def cr_lessons():
    if request.method == "GET":
        return render_template("create_lessons.html")
    if request.method == "POST":
        print("Tulee postiin")
        date = request.form["date"]
        time = int(request.form["time"])
        max = int(request.form["max"])
        level = int(request.form["level"])
        print("Arvot tallentuvat")
        if lessons.create(date,time,max,level,db):
            return redirect("/lessons")
        else:
            return render_template("error.html", message = "Virhe tunnin luonnissa.")

#if __name__ == "__main__":
#    app.run(debug=True)
