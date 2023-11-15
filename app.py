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
    return render_template("schedule.html", subjects=subjects)


@app.route("/update")
def updateSchedule():
    return render_template("index.html")