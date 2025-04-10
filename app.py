from flask import Flask, render_template, request, redirect
import mysql.connector

app=Flask(__name__)

def get_db_connection():
    return  mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="control_tareas"
    )

@app.route("/")
def base():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    conn.close()
    return render_template("index.html",actividades=tareas)


