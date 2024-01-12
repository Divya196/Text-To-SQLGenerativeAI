from dotenv  import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai 

#Configure genai key

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

#Function to load google gemini model

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

#Function to retrieve query from the database

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#Defining prompt

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name EMPLOYEE and has the following columns - NAME, TEAM, 
    DOMAIN \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM EMPLOYEE ;
    \nExample 2 - Tell me all the employees working in MLOPS team?, 
    the SQL command will be something like this SELECT * FROM EMPLOYEE 
    where TEAM="MLOPS"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

#streamlit Application

st.set_page_config(page_title = "I can retrieve any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input : ", key = "input")

submit = st.button("Ask the Question")

#if submit button is clicked

if submit:
    response = get_gemini_response(question,prompt)
    print(response)
    response = read_sql_query(response,"employee.db")
    st.subheader("THE RESPONSE IS")
    for row in response:
        print(row)
        st.header(row)
    
