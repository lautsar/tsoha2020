#from db import db
from flask import session
import os
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password,db):
    sql = "SELECT password, id, name, role, level, confirmed FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            session["user_name"] = user[2]
            session["user_role"] = user[3]
            session["csrf_token"] = os.urandom(16).hex()
            
            if user[5] == True:
                session["user_level"] = user[4]
            else:
                session["user_level"] = 1

            return True
        else:
            return False

def logout():
    del session["user_id"]
    del session["user_name"]
    del session["user_level"]
    del session["user_role"]
    del session["csrf_token"]

def register(username,password,name,email,level,db):
    sql = "SELECT 1 FROM users WHERE username = :username"
    result = db.session.execute(sql, {"username":username})
    
    if result.fetchone() != None:
        return False

    hash_value = generate_password_hash(password)

    sql = "INSERT INTO users (username,password,name,email,level,confirmed,role) VALUES (:username,:password,:name,:email,:level,:confirmed,:role)"
    db.session.execute(sql, {"username":username,"password":hash_value,"name":name,"email":email,"level":level,"confirmed":'0',"role":1})
    db.session.commit()

    return login(username,password,db)

def list_unconfirmed(db):
    sql = "SELECT id, name, level FROM users WHERE confirmed = 'f'"
    result = db.session.execute(sql)
    users = result.fetchall()
    return users

def confirm_level(id, level, db):
    sql = "UPDATE users SET level = :level, confirmed = 't'  WHERE id = :id"
    db.session.execute(sql, {"id":id, "level":level})
    db.session.commit()
    return True

def set_role(username, role, db):
    sql = "SELECT 1 FROM users WHERE username = :username"
    result = db.session.execute(sql, {"username":username})
    
    if result.fetchone() == None:
        return False

    sql = "UPDATE users SET role = :role WHERE username = :username"
    db.session.execute(sql, {"role":role, "username":username})
    db.session.commit()
    return True

def get_user_info(id, db):
    sql = "SELECT name, username, level, confirmed, role FROM users WHERE id = :id"
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()

def user_id():
    return session.get("user_id",0)

def user_name():
    return session.get("user_name",0)

def user_role():
    return session.get("user_role",0)

def user_level():
    return session.get("user_level",0)
