import sqlite3

def connect_database():
    return sqlite3.connect("AMS.db")

def create_table():
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_data
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    studentID TEXT NOT NULL,
    fullname TEXT NOT NULL,
    birthdate TEXT NOT NULL,
    grade TEXT NOT NULL,     
    guardian TEXT NOT NULL,
    contact TEXT NOT NULL,
    emergencycontact TEXT NOT NULL, 
    allergies TEXT NOT NULL                           
    )
    """)
    conn.commit()
    conn.close()

def insert_data(studentID, fullname, birthdate, grade, guardian, contact, emergencycontact, allergy):
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO student_data(studentID, fullname, birthdate, grade, guardian, contact, emergencycontact, allergy) VALUES (?,?)",(studentID, fullname, birthdate, grade, guardian, contact, emergencycontact, allergy))

        conn.commit()
        conn.close()


create_table()
