# Simple Flask + SQLite app

A local notes app. Add and delete notes in your browser. SQLite is included with Python, and the database is created automatically as `notes.db` beside `app.py`.

Requires Python 3.9 or newer.

## Run on Windows (PowerShell)

Open a terminal in this folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

Open http://127.0.0.1:5000 in your browser. Press Ctrl+C in the terminal to stop.

To start it again, run only the last command. No virtual environment activation is needed.

## Run on macOS / Linux

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python app.py
```

Notes persist when you restart the app. This is a minimal local app without user accounts.
