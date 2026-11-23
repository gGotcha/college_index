from pathlib import Path
import sqlite3

from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)
DATABASE = Path(__file__).with_name("notes.db")


def connect_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = connect_db()
    try:
        with connection:
            connection.execute(
                "CREATE TABLE IF NOT EXISTS notes "
                "(id INTEGER PRIMARY KEY, text TEXT NOT NULL)"
            )
    finally:
        connection.close()


@app.route("/", methods=["GET", "POST"])
def index():
    connection = connect_db()
    try:
        if request.method == "POST":
            text = request.form.get("text", "").strip()
            if text:
                with connection:
                    connection.execute("INSERT INTO notes (text) VALUES (?)", (text,))
            return redirect(url_for("index"))
        notes = connection.execute("SELECT * FROM notes ORDER BY id DESC").fetchall()
        return render_template("index.html", notes=notes)
    finally:
        connection.close()


@app.post("/delete/<int:note_id>")
def delete_note(note_id):
    connection = connect_db()
    try:
        with connection:
            connection.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    finally:
        connection.close()
    return redirect(url_for("index"))


init_db()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
