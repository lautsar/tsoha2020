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
        email = request.form["email"]
        level = int(request.form["level"])
        
        if users.register(username,password,name,email,level,db):
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
    if users.user_role() == 0:
        return render_template("error.html", message = "Ei oikeutta nähdä sivua.")

    users.logout()
    return redirect("/")

@app.route("/purchase", methods=["get","post"])
def purchase():
    if users.user_role() == 0:
        return render_template("error.html", message = "Ei oikeutta nähdä sivua.")

    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)

        user_id = session["user_id"]
        times = int(request.form["card"])
        cards.new(user_id,times,db)
        return render_template("success.html", message = "Osto onnistui.")
    if request.method == "GET":    
        return render_template("purchase.html")

@app.route("/listlessons")
def ls_lessons():
    user_id = users.user_id()
    tunnit = lessons.get_list(user_id, db)
    level = users.user_level()
    return render_template("list_lessons.html", lessons=tunnit, level=level)

@app.route("/reservations")
def ls_reservations():
    if users.user_role() == 0:
        return render_template("error.html", message = "Ei oikeutta nähdä sivua.")

    user_id = session["user_id"]
    reservations = lessons.list_reservations(user_id, db)
    past = lessons.list_past(user_id, db)
    return render_template("reservations.html", lessons=reservations, past=past)

@app.route("/book", methods=["get","post"])
def book():
    if request.method == "GET":
        return render_template("error.html", message = "Ei oikeutta nähdä sivua.")

    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)

        user_id = session["user_id"]
        user_level = session["user_level"]
        lesson_id = int(request.form["id"])
        lesson_level = int(request.form["level"])
        lesson_reservations = int(request.form["reservations"])
        lesson_reserved = request.form["reserved"]
        lesson_max = int(request.form["max"])
        tunnit = lessons.get_list(user_id, db)
        
        if lesson_reserved != 'None':
            return render_template("list_lessons.html", lessons=tunnit, level=user_level, message = "Olet jo varannut tämän tunnin.")

        if lesson_reservations >= lesson_max:
            return render_template("list_lessons.html", lessons=tunnit, level=user_level, message = "Valitsemasi tunti on täynnä.")

        if lesson_level > user_level:
            return render_template("list_lessons.html", lessons=tunnit, level=user_level, message = "Tasosi ei riitä valitsemallesi tunnille.")

        if lessons.number(user_id,db) >= cards.bought_cards(user_id,db):
            return render_template("list_lessons.html", lessons=tunnit, level=user_level, message = "Ei jäljellä olevia kertoja kortissa.")
        
        lessons.book_lesson(user_id,lesson_id,db)
        return render_template("success.html", message = "Tunnin varaus onnistui.")

@app.route("/cancel_res", methods=["get","post"])
def cancel_res():
    if request.method == "GET":
        return render_template("error.html", message = "Ei oikeutta nähdä sivua.")

    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)

        user_id = session["user_id"]
        lesson_id = int(request.form["id"])
        
        if lessons.cancel_reservation(user_id,lesson_id,db):
            return render_template("success.html", message = "Tunnin peruminen onnistui.")
        else:
            return render_template("error.html", message = "Tunnin peruminen ei ole enää mahdollista.")

@app.route("/lessons", methods=["get","post"])
def cr_lessons():
    if users.user_role() == 0 or users.user_role() == 1:
        return render_template("error.html", message = "Ei oikeutta nähdä sivua.")

    if request.method == "GET":
        return render_template("create_lessons.html")
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)

        date = request.form["date"]
        time = int(request.form["time"])
        max = int(request.form["max"])
        level = int(request.form["level"])
        id = users.user_id()
        
        if lessons.create(date,time,max,level,id,db):
            return render_template("success.html", message = "Tunnin lisäys onnistui.")
            #return redirect("/lessons")
        else:
            return render_template("error.html", message = "Virhe tunnin luonnissa.")

@app.route("/confirm", methods=["get","post"])
def confirm():
    if users.user_role() == 0 or users.user_role() == 1:
        return render_template("error.html", message = "Ei oikeutta nähdä sivua.")

    if request.method == "GET":
        unconfirmed = users.list_unconfirmed(db)
        return render_template("confirm.html", users = unconfirmed)
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)

        id = request.form["id"]
        level = request.form["level"]
        users.confirm_level(id, level, db)

        return render_template("success.html", message = "Käyttäjän taso vahvistettu.")

@app.route("/set_role", methods=["get","post"])
def set_role():
    if users.user_role() != 3:
        return render_template("error.html", message = "Ei oikeutta nähdä sivua.")

    if request.method == "GET":
        return render_template("set_role.html")
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)

        username = request.form["username"]
        role = request.form["role"]

        if users.set_role(username, role, db):
            return render_template("success.html", message = "Käyttäjän rooli muutettu.")
        else:
            return render_template("error.html", message = "Käyttäjää ei löydy.")

@app.route("/info")
def info():
    if users.user_role() == 0:
        return render_template("error.html", message = "Ei oikeutta nähdä sivua.")

    user = users.user_id()

    card = cards.get_cards(user,db)
    bought = cards.bought_cards(user,db)

    return render_template("info.html", cards=card, bought=bought)