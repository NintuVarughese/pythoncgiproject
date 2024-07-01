#!C:\Users\cclab23\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import sqlite3

# Function to create database table if not exists
def create_table():
    conn = sqlite3.connect('data_db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 age INTEGER NOT NULL,
                 course TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(name, age, course):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    conn.close()

# Function to fetch all data from the database
def fetch_data():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    conn.close()
    return rows

# Function to update data in the database
def update_data(id, name, age, course):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?", (name, age, course, id))
    conn.commit()
    conn.close()

# Function to delete data from the database
def delete_data(id):
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Main CGI script to handle form submission
def main():
    form = cgi.FieldStorage()
    if form.getvalue('submit'):
        name = form.getvalue('name')
        age = form.getvalue('age')
        course = form.getvalue('course')
        
        create_table()  # Ensure table exists
        
        # Insert data into database
        insert_data(name, age, course)
        
        # Redirect or display success message (HTML response)
        print("Content-type: text/html\n\n")
        print("<html>")
        print("<head>")
        print("<title>Success</title>")
        print("</head>")
        print("<body>")
        print("<h2>Data submitted successfully!</h2>")
        print("<p><a href='index.html'>Go Back</a></p>")
        print("</body>")
        print("</html>")

# Execute main function
if __name__ == "__main__":
    main()
