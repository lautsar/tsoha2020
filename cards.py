#from db import db
from flask import session
#from werkzeug.security import check_password_hash, generate_password_hash

def new(user,times,db):
    try:
        sql = "INSERT INTO cards (times,valid,user_id) VALUES (:times,:valid,:user_id)"
        db.session.execute(sql, {"times":times,"valid":'2020-08-31',"user_id":user})
        db.session.commit()
    except:
        return False
    return True