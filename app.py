import psycopg2

DB_CONFIG = {
    "dbname": "student_db",
    "user": "postgres",      
    "password": "<your_password>",
    "host": "localhost",
    "port": "5432"
}

def getAllStudents():
    """
    Retrieves and displays all records from the students table.
    Connects to PostgreSQL, executes a SELECT query, and prints each row.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    
    print("\n--- Current Students in Database ---")
    for row in rows:
        print(row)
        
    cur.close()
    conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """
    Inserts a new student record into the students table using parameterized queries 
    to prevent SQL injection. Commits the transaction to save changes.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    query = """
        INSERT INTO students (first_name, last_name, email, enrollment_date) 
        VALUES (%s, %s, %s, %s);
    """
    cur.execute(query, (first_name, last_name, email, enrollment_date))
    conn.commit()
    
    print(f"\n[SUCCESS] Added new student: {first_name} {last_name}")
    
    cur.close()
    conn.close()

def updateStudentEmail(student_id, new_email):
    """
    Updates the email address for a student matching the specified student_id.
    Commits the changes to the database.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    query = "UPDATE students SET email = %s WHERE student_id = %s;"
    cur.execute(query, (new_email, student_id))
    conn.commit()
    
    print(f"\n[SUCCESS] Updated email for student ID {student_id} to {new_email}")
    
    cur.close()
    conn.close()

def deleteStudent(student_id):
    """
    Deletes the student record matching the specified student_id from the database.
    Commits the transaction.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    
    query = "DELETE FROM students WHERE student_id = %s;"
    cur.execute(query, (student_id,))
    conn.commit()
    
    print(f"\n[SUCCESS] Deleted student ID {student_id}")
    
    cur.close()
    conn.close()

if __name__ == "__main__":
    print("Running application functions...")
    getAllStudents()
    