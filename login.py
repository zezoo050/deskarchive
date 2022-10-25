def login(user,pas):
    import sqlite3 as db
    from datetime import datetime
    conn = db.connect(r'data\db1.db')
    cursor = conn.cursor()
    try :
        cursor = conn.execute(f"select user_id , users_name , user_pass,user_prem from users where users_name = '{user}' and user_pass = '{pas}'")
        row = cursor.fetchall()
        row = row[0]
    except:
        return False , 0 , 0
    else:
        if str(row[1]) == str(user) and str(row[2]) == str(pas):
            if row[3] == 3:
                return False , 0 , 0
            else:
                now = datetime.now()
                now = now.strftime("%d/%m/%Y  %H:%M")
                cursor.execute(f"insert into log (user_id,time) values (?,?) ", (row[0],now))
                conn.commit()
                return True , row[0] , row[3]
        else:
            return False , 0 , 0
if __name__ == '__main__':
    login()