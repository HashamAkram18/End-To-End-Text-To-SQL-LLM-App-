from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text 

# Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    print(f"Executing SQL query: {sql}")
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns
    - NAME, CLASS, SECTION, MARKS 
    SECTION \n\nFor example,
    \nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]



st.set_page_config(page_title="I can Retrieve Any SQL Query")
st.header("Gemini App: Retrieve SQL Data")

question = st.text_input("Enter your question:", key="input")

if st.button("Ask the question"):
  # Use a try-except block to handle potential errors
  try:
    response = get_gemini_response(question, prompt)
    sql_query = response.strip()  # Remove potential leading/trailing whitespace

    # **Pre-process the response to remove unwanted characters:**
    sql_query = sql_query.replace("```", "").replace("sql", "")

    # Execute the query and display the results
    results = read_sql_query(sql_query, "student.db")
    st.subheader("The Response:")
    for row in results:
      st.write(row)  # Use st.write() for displaying individual rows

  except Exception as e:
    st.error(f"An error occurred: {e}")

