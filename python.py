#!C:\Users\cclab23\AppData\Local\Programs\Python\Python312\python.exe
import cgi
import mysql.connector

# Function to create database table if not exists
def create_table():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Replace with your MySQL password
        database="data_db"
    )
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS students (
                 id INT AUTO_INCREMENT PRIMARY KEY,
                 name VARCHAR(255) NOT NULL,
                 age INT NOT NULL,
                 course VARCHAR(255) NOT NULL
                 )''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(name, age, course):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Replace with your MySQL password
        database="data_db"
    )
    c = conn.cursor()
    sql = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    val = (name, age, course)
    c.execute(sql, val)
    conn.commit()
    conn.close()

# Function to fetch all data from the database
def fetch_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Replace with your MySQL password
        database="data_db"
    )
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    rows = c.fetchall()
    conn.close()
    return rows

# Function to update data in the database
def update_data(id, name, age, course):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Replace with your MySQL password
        database="data_db"
    )
    c = conn.cursor()
    sql = "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s"
    val = (name, age, course, id)
    c.execute(sql, val)
    conn.commit()
    conn.close()

# Function to delete data from the database
def delete_data(id):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Replace with your MySQL password
        database="data_db"
    )
    c = conn.cursor()
    sql = "DELETE FROM students WHERE id=%s"
    val = (id,)
    c.execute(sql, val)
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
