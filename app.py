from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

subjects = ["ITEC 101",
            "ITEC 102",
            "GEC 101",
            "GEC 102",
            "PI 100",
            "KOMFIL",
            "PATHFIT 1" 
]

@app.route("/")
def showSchedule():
    # Connect to the SQLite database
    connection = sqlite3.connect('schedule.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Fetch the schedule data from the database
    cursor.execute('SELECT * FROM schedule')
    schedule_data = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Render a template with the schedule data
    return render_template('schedule.html', schedule=schedule_data)


@app.route("/update")
def updateSchedule():
    return render_template("index.html")