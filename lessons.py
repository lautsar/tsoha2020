#from db import db
from flask import session
#from werkzeug.security import check_password_hash, generate_password_hash

def create(date,time,max,level,db):
    try:
        print("1")
        sql = "INSERT INTO lessons (date,time,max,level) VALUES (:date,:time,:max,:level)"
        print("2")
        db.session.execute(sql, {"date":date,"time":time,"max":max,"level":level})
        print("3")
        db.session.commit()
    except:
        print("4")
        return False
    return True

def get_list(db):
    try:
        sql = "SELECT * FROM lessons"
        result = db.session.execute(sql)
    except:
        return False
    return result.fetchall()