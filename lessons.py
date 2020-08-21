#from db import db
from flask import session
#from werkzeug.security import check_password_hash, generate_password_hash

def create(date,time,max,level,db):
    try:
        sql = "INSERT INTO lessons (date,time,max,level) VALUES (:date,:time,:max,:level)"
        db.session.execute(sql, {"date":date,"time":time,"max":max,"level":level})
        db.session.commit()
    except:
        return False
    return True

def get_list(db):
    try:
        #sql = "SELECT * FROM lessons WHERE date >= current_date ORDER BY date, time"
        #sql = "SELECT L.id, L.date, L.time, L.level, L.max, COALESCE(C.res,0) FROM lessons L LEFT JOIN (SELECT lesson_id AS id, COUNT(user_id) AS res FROM users_lessons GROUP BY lesson_id) AS C ON L.id = C.id WHERE date >= current_date ORDER BY date, time;"
        sql = "SELECT L.id, L.date, L.time, L.level, L.max, COALESCE(C.res,0), D.user_id FROM lessons L LEFT JOIN (SELECT lesson_id AS id, COUNT(user_id) AS res FROM users_lessons GROUP BY lesson_id) AS C ON L.id = C.id LEFT JOIN (SELECT * FROM users_lessons WHERE user_id = 39) as D ON L.id = D.lesson_id WHERE date >= current_date ORDER BY date, time;"
        result = db.session.execute(sql)
    except:
        return False
    return result.fetchall()

def book_lesson(user_id,lesson_id,db):
    try:
        sql = "INSERT INTO users_lessons (user_id,lesson_id) VALUES (:user_id,:lesson_id)"
        db.session.execute(sql, {"user_id":user_id,"lesson_id":lesson_id})
        db.session.commit()
    except:
        return False
    return True

def list_reservations(user_id, db):
    try:
        sql = "SELECT L.id, L.date, L.time, L.level FROM users U LEFT JOIN users_lessons ON U.id = user_id LEFT JOIN lessons L on lesson_id = L.id WHERE L.date >= current_date AND U.id = :user_id ORDER BY date, time;"
        result = db.session.execute(sql, {"user_id":user_id})
    except:
        return False
    return result.fetchall()

#def list_participants(user_id, user_status, db):
#    SELECT L.date, L.time, L.level, U.name FROM lessons L, users_lessons J, users U WHERE L.date >= current_date AND J.user_id = U.id AND J.lesson_id = L.id; 
