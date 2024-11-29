import sqlite3

def create_user(email, name, password):
    conn= sqlite3.connect('./data/database.db')
    cursor =conn.cursor()
    cursor.execute('INSERT INTO user (email, name, password) values(?,?,?)', (email,name,password))
    conn.commit()
    conn.close()

def find_user_by_email(email):
    conn=sqlite3.connect('./data/database.db')
    cursor= conn.cursor()
    cursor.execute('SELECT email, name, password From user WHERE email=?', (email,))
    user=cursor.fetchone()
    conn.close()
    return user 

def find_user_user_by_email_and_password(email,password):
    conn=sqlite3.connect('./data/database.db')
    cursor=conn.cursor()
    cursor.execute('SELECT email, name, password From user WHERE email=?', (email,))
    user=cursor.fetchone()
    return user 

#create_user('alexluong2703@gail.com', "TRi Cuong", "2703")
print(find_user_by_email('alexluong2703@gail.com'))
print(find_user_user_by_email_and_password('alexluong2703@gail.com','2703'))