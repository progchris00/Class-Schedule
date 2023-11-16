from flask import Flask, render_template, request, g, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

subjects = ["ITEC 101",
            "PI 100",
            "PATHFIT 1"
]

todaysDay= datetime.now().strftime('%A')

@app.route("/")
def showSchedToday():
    # Connect to the SQLite database
    connection = sqlite3.connect('schedule.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    # Fetch the schedule data from the database
    cursor.execute(f"SELECT * FROM schedule WHERE day = '{todaysDay}' ")
    schedule_data = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Render a template with the schedule data
    return render_template('schedule.html', schedule=schedule_data, todaysDay=todaysDay)


@app.route("/setschedule", methods=["POST"])
def setSchedule():
    currentdate = request.form.get('currentdate')

    connection = sqlite3.connect('schedule.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    for subject in subjects:
        room = request.form.get(f'room_{subject}')
        modality = request.form.get(f'modality_{subject}')
        time = request.form.get(f'time_{subject}')

        cursor.execute(f"INSERT INTO schedule (subject_name, date, time, room, modality, is_default) VALUES ('{subject}', '{currentdate}', '{time}', '{room}', '{modality}', 'false'); ")
        connection.commit()

    connection.close()
    return redirect(url_for('showschedule'))

@app.route("/showschedule")
def showschedule():
    currentdate = datetime.now().strftime('%Y-%m-%d')
    connection = sqlite3.connect('schedule.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM schedule WHERE date = '{currentdate}' AND is_default = 'false' ")
    schedule_data = cursor.fetchall()

    return render_template('showschedule.html', schedule=schedule_data)