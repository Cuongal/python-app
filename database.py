import sqlite3
from datetime import datetime, timedelta

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_schedule_by_date(date_str):
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.row_factory = dict_factory
    
    print(f"Searching for schedule on date: {date_str}")  # Debug print
    
    # First check if we have any data in the table
    cursor.execute('SELECT COUNT(*) as count FROM schedule')
    count = cursor.fetchone()['count']
    print(f"Total records in schedule table: {count}")  # Debug print
    
    # Get schedule for the specific date
    cursor.execute('''
    SELECT subject, start_time, end_time, teacher, room, type 
    FROM schedule 
    WHERE date = ? 
    ORDER BY start_time
    ''', (date_str,))
    
    schedule = cursor.fetchall()
    print(f"Found {len(schedule)} items for date {date_str}")  # Debug print
    
    if len(schedule) == 0:
        # Debug: show a sample of dates in the database
        cursor.execute('SELECT DISTINCT date FROM schedule LIMIT 5')
        sample_dates = cursor.fetchall()
        print("Sample dates in database:", [d['date'] for d in sample_dates])
    
    conn.close()
    return schedule

def create_user(email, name, password):
    conn= sqlite3.connect('./data/database.db')
    cursor =conn.cursor()
    cursor.execute('INSERT INTO user (email, name, password) values(?,?,?)', (email,name,password))
    conn.commit()
    conn.close()

def find_user_by_email(email):
    conn= sqlite3.connect('./data/database.db')
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
    cursor.execute('SELECT id, email, name, password, avatar, birthday, gender From user WHERE id=?',(user_id,))
    user=cursor.fetchone()
    conn.close()
    return user

def update_user(user_id, name, birthday, gender):
    conn= sqlite3.connect('./data/database.db')
    cursor=conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('UPDATE user SET name=?, birthday=?, gender=? WHERE id=?',(name,birthday,gender,user_id))
    conn.commit()
    conn.close()

# Application functions
def create_application(data):
    """Create a new application"""
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO applications (
            user_id, type, recipient, title, content, 
            start_date, end_date, status, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['user_id'], data['type'], data['recipient'], 
            data['title'], data['content'], data['start_date'], 
            data['end_date'], data['status'], datetime.now().isoformat()
        ))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error creating application: {e}")
        return False
    finally:
        conn.close()

def get_application_by_id(app_id):
    """Get application by id"""
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT * FROM applications WHERE id = ?', (app_id,))
    app = cursor.fetchone()
    conn.close()
    return app

def get_applications_by_user_id(user_id):
    """Get all applications for a user"""
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    cursor.row_factory = dict_factory
    cursor.execute('SELECT * FROM applications WHERE user_id = ? ORDER BY created_at DESC', (user_id,))
    apps = cursor.fetchall()
    conn.close()
    return apps

def update_application(data):
    """Update an application"""
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        UPDATE applications 
        SET type = ?, recipient = ?, title = ?, content = ?,
            start_date = ?, end_date = ?, status = ?
        WHERE id = ?
        ''', (
            data['type'], data['recipient'], data['title'],
            data['content'], data['start_date'], data['end_date'],
            data.get('status', 'pending'), data['id']
        ))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error updating application: {e}")
        return False
    finally:
        conn.close()

def delete_application(app_id):
    """Delete an application"""
    if not app_id:
        return False
        
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM applications WHERE id = ?', (app_id,))
        if cursor.rowcount == 0:  # No rows were deleted
            return False
        conn.commit()
        return True
    except Exception as e:
        print(f"Error deleting application: {e}")
        return False
    finally:
        conn.close()
