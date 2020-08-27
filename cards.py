#from db import db
from flask import session

def new(user,times,db):
    sql = "INSERT INTO cards (times,bought,user_id) VALUES (:times,current_date,:user_id)"
    db.session.execute(sql, {"times":times,"user_id":user})
    db.session.commit()
    return True

def get_cards(user,db):
    sql = "SELECT bought, times FROM cards WHERE user_id = :user_id ORDER BY id;"
    result = db.session.execute(sql, {"user_id":user})
    cards = result.fetchall()
    return cards

def bought_cards(user,db):
    sql = "SELECT SUM(times) FROM cards WHERE user_id = :user_id;"
    result = db.session.execute(sql, {"user_id":user})
    bought = result.fetchone()

    if bought[0] != None:
        return bought[0]
    else:
        return 0