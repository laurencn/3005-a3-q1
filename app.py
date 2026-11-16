import psycopg2

DB_CONFIG = {
    "dbname": "student_db",
    "user": "postgres",
    "password": "your_password",  
    "host": "localhost",
    "port": "5432"
}

def getAllStudents():
    """Retrieves and displays all records from the students table."""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    cur.execute("SELECT * FROM students ORDER BY student_id ASC;")
    rows = cur.fetchall()
    print("\n--- Current Students ---")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def addStudent(first_name, last_name, email, enrollment_date):
    """Inserts a new student record into the students table."""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
    cur.execute(query, (first_name, last_name, email, enrollment_date))
    conn.commit()
    print(f"\n[SUCCESS] Added: {first_name} {last_name}")
    cur.close()
    conn.close()

def updateStudentEmail(student_id, new_email):
    """Updates the email address for a student with the specified student_id."""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    query = "UPDATE students SET email = %s WHERE student_id = %s;"
    cur.execute(query, (new_email, student_id))
    conn.commit()
    print(f"\n[SUCCESS] Updated email for ID {student_id} to {new_email}")
    cur.close()
    conn.close()

def deleteStudent(student_id):
    """Deletes the record of the student with the specified student_id."""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    query = "DELETE FROM students WHERE student_id = %s;"
    cur.execute(query, (student_id,))
    conn.commit()
    print(f"\n[SUCCESS] Deleted student ID {student_id}")
    cur.close()
    conn.close()

if __name__ == "__main__":
    while True:
        print("\n=== Student Database Menu ===")
        print("1. Get All Students")
        print("2. Add Student")
        print("3. Update Student Email")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == "1":
            getAllStudents()
        elif choice == "2":
            fn = input("First Name: ")
            ln = input("Last Name: ")
            em = input("Email: ")
            dt = input("Enrollment Date (YYYY-MM-DD): ")
            addStudent(fn, ln, em, dt)
        elif choice == "3":
            sid = int(input("Student ID to update: "))
            new_em = input("New Email: ")
            updateStudentEmail(sid, new_em)
        elif choice == "4":
            sid = int(input("Student ID to delete: "))
            deleteStudent(sid)
        elif choice == "5":
            break