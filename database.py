import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_user(email, name, password):
    conn= sqlite3.connect('./data/database.db')
    cursor =conn.cursor()
    cursor.execute('INSERT INTO user (email, name, password) values(?,?,?)', (email,name,password))
    conn.commit()
    conn.close()

def find_user_by_email(email):
    conn=sqlite3.connect('./data/database.db')
    cursor= conn.cursor()
    cursor.row_factory = dict_factory 
    cursor.execute('SELECT id, email, name, password From user WHERE email=?', (email,))
    user=cursor.fetchone()
    conn.close()
    return user 

def find_user_user_by_email_and_password(email,password):
    conn=sqlite3.connect('./data/database.db')
    cursor=conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT id, email, name, password From user WHERE email=? AND password=?', (email,password, ))
    user=cursor.fetchone()
    return user 


def update_user_avatar(user_id, avatar):
    conn= sqlite3.connect('./data/database.db')
    cursor=conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('UPDATE user SET avatar=?WHERE id+?',(avatar,user_id))
    conn.commit()
    conn.close()
  
def find_user_by_id(user_id):
    conn= sqlite3.connect('./data/database.db')
    cursor=conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT id, email, name, password From user WHERE id=?',(user_id,))
    user=cursor.fetchone()
    conn.close()
    return user

# create_user('alexluong2703@gail.com', "TRi Cuong", "2703")
print(find_user_by_email('alexluong2703@gail.com'))
print(find_user_user_by_email_and_password('alexluong2703@gail.com','2703'))
print('hello')