from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)


@app.route("/")
def showSchedule():
    return render_template("schedule.html")


@app.route("/update")
def updateSchedule():
    return render_template("index.html")