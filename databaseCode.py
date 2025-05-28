
import sqlite3

DB_NAME = "students.db"

def connect_db():
    """Connect to the SQLite3 database."""
    return sqlite3.connect(DB_NAME)

def create_students_table():
    """Create the students table with all fields."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            full_name TEXT NOT NULL,
            sex TEXT CHECK(sex IN ('Male', 'Female')),
            parent_name TEXT,
            occupation TEXT,
            phone TEXT,
            grade TEXT CHECK(grade IN (
                'Grade 1','Grade 2','Grade 3','Grade 4','Grade 5','Grade 6',
                'Grade 7','Grade 8','Grade 9','Grade 10','Grade 11','Grade 12'
            )),
            photo_path TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_student(student_id, full_name, sex, parent_name, occupation, phone, grade, photo_path=None):
    """Insert a new student record."""
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO students (
                student_id, full_name, sex, parent_name, occupation, phone, grade, photo_path
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (student_id, full_name, sex, parent_name, occupation, phone, grade, photo_path))
        conn.commit()
    except sqlite3.IntegrityError as e:
        raise ValueError(f"Student ID already exists or invalid data: {e}")
    finally:
        conn.close()
    
def student_exists(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM students WHERE student_id = ?", (student_id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists


def get_all_students():
    """Return a list of all students."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    conn.close()
    return results

def delete_student(student_id):
    """Delete a student by ID."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
    conn.commit()
    conn.close()

def update_student(student_id, full_name, sex, parent_name, occupation, phone, grade, photo_path=None):
    """Update a student's record."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE students SET
            full_name = ?,
            sex = ?,
            parent_name = ?,
            occupation = ?,
            phone = ?,
            grade = ?,
            photo_path = ?
        WHERE student_id = ?
    """, (full_name, sex, parent_name, occupation, phone, grade, photo_path, student_id))
    conn.commit()
    conn.close()
