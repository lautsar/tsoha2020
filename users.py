#from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password,db):
#    sql = "SELECT password, id FROM users WHERE username=:username"
    sql = "SELECT password, id, name FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            session["user_name"] = user[2]#
            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["user_name"]

def register(username,password,name,level,db):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username,password,name,email,level,confirmed,admin,teacher) VALUES (:username,:password,:name,:email,:level,:confirmed,:admin,:teacher)"
        db.session.execute(sql, {"username":username,"password":hash_value,"name":name,"email":"email","level":level,"confirmed":'0',"admin":'0',"teacher":'0'})
        db.session.commit()
    except:
        print("4")
        return False
    return login(username,password,db)

def user_id():
    return session.get("user_id",0)

def user_name():
    return session.get("user_name")
