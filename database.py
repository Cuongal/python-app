import sqlite3
from datetime import datetime, timedelta

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def create_tables():
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    
    # Drop and recreate only schedule table
    cursor.execute('DROP TABLE IF EXISTS schedule')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS schedule (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        subject TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        teacher TEXT NOT NULL,
        room TEXT NOT NULL,
        type TEXT DEFAULT 'normal'
    )
    ''')
    
    conn.commit()
    conn.close()
    print("Schedule table dropped and recreated successfully")

def generate_april_schedule():
    # Danh sách môn học và giáo viên
    morning_subjects = [
        ("Toán", "Bùi Thị Lan", "Phòng A101"),
        ("Ngữ Văn", "Phạm Đăng Dung", "Phòng A102"),
        ("Tiếng Anh", "Emily Williams", "Phòng A103"),
        ("Vật Lý", "Lê Kim Anh", "Phòng B101"),
        ("Hóa Học", "Mai Quốc Duy", "Phòng B102"),
        ("Sinh Học", "Trần An Khang", "Phòng B103"),
        ("Địa Lý", "Lê Hiếu", "Phòng C101"),
        ("GDCD", "Nguyễn Huyền Trang", "Phòng C102"),
        ("Thể Dục", "James Anderson", "Sân thể thao"),
        ("GDQP", "Đỗ Minh Tuấn", "Phòng C103")
    ]

    schedule_data = []
    start_date = datetime(2025, 4, 1)  # Changed to 2025
    end_date = datetime(2025, 4, 30)   # Changed to 2025
    current_date = start_date

    while current_date <= end_date:
        if current_date.weekday() < 5:  # 0-4 là thứ 2 đến thứ 6
            morning_times = [
                ("07:00", "07:45"),
                ("07:45", "08:30"),
                ("08:45", "09:30"),
                ("09:30", "10:15"),
                ("10:15", "11:00")
            ]

            afternoon_times = [
                ("13:00", "13:45"),
                ("13:45", "14:30"),
                ("14:30", "15:15"),
                ("15:45", "16:30"),
                ("16:30", "17:15")
            ]

            import random
            daily_subjects = random.sample(morning_subjects, len(morning_subjects))
            
            # Thêm các tiết sáng
            for i, time_slot in enumerate(morning_times):
                subject, teacher, room = daily_subjects[i]
                schedule_data.append((
                    current_date.strftime('%Y-%m-%d'),
                    subject,
                    time_slot[0],
                    time_slot[1],
                    teacher,
                    room,
                    'normal'
                ))
                
                # Thêm giải lao sau tiết 2
                if i == 1:
                    schedule_data.append((
                        current_date.strftime('%Y-%m-%d'),
                        'Giải lao',
                        '08:30',
                        '08:45',
                        '',
                        '',
                        'break'
                    ))

            # Thêm các tiết chiều
            daily_subjects = random.sample(morning_subjects, len(morning_subjects))
            for i, time_slot in enumerate(afternoon_times):
                subject, teacher, room = daily_subjects[i]
                schedule_data.append((
                    current_date.strftime('%Y-%m-%d'),
                    subject,
                    time_slot[0],
                    time_slot[1],
                    teacher,
                    room,
                    'normal'
                ))
                
                # Thêm giải lao sau tiết 8 (tiết 3 buổi chiều)
                if i == 2:
                    schedule_data.append((
                        current_date.strftime('%Y-%m-%d'),
                        'Giải lao',
                        '15:15',
                        '15:45',
                        '',
                        '',
                        'break'
                    ))

        current_date += timedelta(days=1)

    return schedule_data

def insert_sample_schedule():
    conn = sqlite3.connect('./data/database.db')
    cursor = conn.cursor()
    
    # Xóa dữ liệu cũ
    cursor.execute('DELETE FROM schedule')
    
    # Tạo dữ liệu mẫu
    schedule_data = generate_april_schedule()
    print(f"Generated {len(schedule_data)} schedule items")  # Debug print
    
    # Thêm dữ liệu mới
    cursor.executemany('''
    INSERT INTO schedule (date, subject, start_time, end_time, teacher, room, type) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', schedule_data)
    
    print(f"Inserted {cursor.rowcount} rows")  # Debug print
    
    conn.commit()
    conn.close()

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
    cursor.execute('SELECT id, email, name, password From user WHERE id=?',(user_id,))
    user=cursor.fetchone()
    conn.close()
    return user

# Initialize database
create_tables()
insert_sample_schedule()

# create_user('alexluong2703@gail.com', "TRi Cuong", "2703")
print(find_user_by_email('alexluong2703@gail.com'))
print(find_user_user_by_email_and_password('alexluong2703@gail.com','2703'))