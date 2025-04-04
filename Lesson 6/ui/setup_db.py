import sqlite3
from models.anime import Anime

def dict_factory(cursor,row):
    d={}
    for idx,col in enumerate(cursor,description):
        d[col[0]]=row[idx]
        return d
    
def create_anime(title,release_date,image,rating,link):
    conn=sqlite3. connect('anime.db')
    conn.row_factory=dict_factory
    c=conn.cursor()
    query=f''' INSERT INTO anime(title,release_date,image,rating,link)
             VALUES('{title}','{release_date}','{image}','{rating}','{link}')"'''
    
    c.execute(query)
    conn.commit()
    conn.close()
    
def get_all_anime():
    conn=sqlite3.connect('anime.db')
    conn.row_factory=dict_factory
    c=conn.cursor()
    query="SELECT id,title,release_date,image,rating,link FROM anime"
    c.execute(query)
    results=c.fetchall()
    conn.close
    return results

def get_anime_by_id(id):
    conn=sqlite3.connect('anime.db')
    conn.row_factory=dict_factory
    c=conn.cursor()
    query=f"SELECT id,title,release_date,image,rating,link FROM anime WHERE id={id}"
    c.execute(query)
    results=c.fetchone()
    conn.close()
    return results

def update_anime(id,anime:Anime):
    conn=sqlite3.connect('anime.db')
    conn.row_factory=dict_factory
    c=conn.cursor
    query=f'''UPDATE anime SET title='{anime.title}',release_date='{anime.release_date}',
             image= '{anime.image}',rating='{anime.rating}',link='{anime.link}'=WHERE id= {id}'''
    c.execute(query)
    conn.commit()
    conn.close()
    
def delete_anime(id):
    conn=sqlite3.connect('anime.db')
    conn.row_factory=dict_factory
    c=conn.cursor()
    query= f"DELETE FROM anime WHERE id={id}"
    c.execute(query)
    conn.commit()
    conn.close()
    
    