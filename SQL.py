import sqlite3
import random

# Connect to the database
connection = sqlite3.connect("student.db")

# Create a cursor object
cursor = connection.cursor()

# Drop the table if it already exists (prevents error)
cursor.execute("DROP TABLE IF EXISTS STUDENT")

# Create the table
table = """CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255), MARKS INTEGER);"""
cursor.execute(table)

# List of names for students
names = ["Aisha", "Bashir", "Chanda", "Daniyal", "Emaan", "Fatima", "Ghulam"]

# Loop to insert multiple students with random marks
for name in names:
  # Generate random marks between 50 and 100
  marks = random.randint(50, 100)

  # Randomly choose a class from "Data Science", "Art", "Music", and "Physics"
  class_options = ["Data Science", "Art", "Music", "Physics", "Design", "Development", "commercial"]
  class_choice = random.choice(class_options)

  # Randomly choose a section from "A", "B", and "C"
  section_options = ["A", "B", "C", "D", "E", "F"]
  section_choice = random.choice(section_options)

  # Construct and execute the INSERT query (use f-strings for cleaner formatting)
  query = f"""INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('{name}', '{class_choice}', '{section_choice}', {marks})"""
  cursor.execute(query)

# Display data inserted
print("\nData Inserted in the table:")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
  # Print each row in a more readable way
  print(f"Name: {row[0]}, Class: {row[1]}, Section: {row[2]}, Marks: {row[3]}")

# Commit the changes and close the connection
connection.commit()
connection.close()

print("\nTable created and data inserted successfully!")
