from flask import Blueprint, render_template
import sqlite3

routes = Blueprint("routes", __name__)

@routes.route("/")
def dashboard():
    conn = sqlite3.connect("threats.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM indicators ORDER BY timestamp DESC LIMIT 20")
    data = cursor.fetchall()
    conn.close()
    return render_template("dashboard.html", data=data)
