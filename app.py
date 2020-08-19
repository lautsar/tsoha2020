from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import users, lessons, cards

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
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
        username = request.form["username"]
        password = request.form["password"]
        name = request.form["name"]
        level = int(request.form["level"])
        
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

@app.route("/purchase", methods=["get","post"])
def purchase():
    if request.method == "POST":
        user_id = session["user_id"]
        times = int(request.form["card"])
        cards.new(user_id,times,db)
        return render_template("success.html", message = "Osto onnistui.")
    if request.method == "GET":    
        return render_template("purchase.html")

@app.route("/listlessons")
def ls_lessons():
    tunnit = lessons.get_list(db)
    level = session["user_level"]
    return render_template("list_lessons.html", lessons=tunnit, level=level)

@app.route("/reservations")
def ls_reservations():
    user_id = session["user_id"]
    reservations = lessons.list_reservations(user_id, db)
    return render_template("reservations.html", lessons=reservations)

@app.route("/book", methods=["get","post"])
def book():
    if request.method == "POST":
        user_id = session["user_id"]
        user_level = session["user_level"]
        lesson_id = int(request.form["id"])
        lesson_level = int(request.form["level"])
        lesson_res = int(request.form["reservations"])
        lesson_max = int(request.form["max"])

        if lesson_res >= lesson_max:
            return render_template("error.html", message = "Valitsemasi tunti on täynnä.")

        if lesson_level > user_level:
            return render_template("error.html", message = "Tasosi ei riitä valitsemallesi tunnille.")
        
        lessons.book_lesson(user_id,lesson_id,db)
        return render_template("success.html", message = "Varaus onnistui.")


@app.route("/lessons", methods=["get","post"])
def cr_lessons():
    if request.method == "GET":
        return render_template("create_lessons.html")
    if request.method == "POST":
        
        date = request.form["date"]
        time = int(request.form["time"])
        max = int(request.form["max"])
        level = int(request.form["level"])
        
        if lessons.create(date,time,max,level,db):
            return render_template("success.html", message = "Tunnin lisäys onnistui.")
            #return redirect("/lessons")
        else:
            return render_template("error.html", message = "Virhe tunnin luonnissa.")

@app.route("/confirm", methods=["get","post"])
def confirm():
    if request.method == "GET":
        unconfirmed = users.list_unconfirmed(db)
        return render_template("confirm.html", users = unconfirmed)
    if request.method == "POST":
        id = request.form["id"]
        level = request.form["level"]
        users.confirm_level(id, level, db)

        return render_template("success.html", message = "Käyttäjän taso vahvistettu.")

#if __name__ == "__main__":
#    app.run(debug=True)
