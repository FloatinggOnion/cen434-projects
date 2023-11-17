import os

import mysql.connector as conn

my_db = conn.connect(
    host = os.environ.get('DB_HOST'),
    user = os.environ.get('DB_USER'),
    password = os.environ.get('DB_PASSWORD')
)

# print(my_db)

my_cursor = my_db.cursor()

# Create a database
# my_cursor.execute('CREATE DATABASE cen434')
my_cursor.execute('USE cen434')

# Create table
my_cursor.execute("CREATE TABLE students (name VARCHAR(255), matno VARCHAR(255))")

# Add data
sql = "INSERT INTO students (name, matno) VALUES (%s, %s)"
val = ("Kathy", "20cj027xxx")
my_cursor.execute(sql, val)

my_db.commit()

print(my_cursor.rowcount, "record inserted.")

# Read data
my_cursor.execute("SELECT name, matno FROM students")

myresult = my_cursor.fetchall()

for x in myresult:
  print(x)

# # Update data
# sql = "UPDATE students SET matno = '20CJ028xxx' WHERE address = '20CJ027xxx'"

# my_cursor.execute(sql)

# my_db.commit()

# print(my_cursor.rowcount, "record(s) affected")

# # Delete data
# sql = "DELETE FROM students WHERE matno = '20cj027xxx'"

# my_cursor.execute(sql)

# my_db.commit()

# print(my_cursor.rowcount, "record(s) deleted")

# # Delete table
# sql = "DROP TABLE students"

# my_cursor.execute(sql)

# # Delete database
# sql = "DROP DATABASE cen434"

# my_cursor.execute(sql)


# # close connection
# my_db.close()