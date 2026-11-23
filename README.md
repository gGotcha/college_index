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

## Deploy with GitHub → Railway

Connect the Railway service to `gGotcha/college_index`, branch `main`, with the repository root as its root directory. Enable automatic deployments from GitHub.

The included `railway.toml` installs the Python requirements using Railpack and starts Gunicorn on `0.0.0.0:$PORT`. Railway supplies `PORT`. The `/` page is also the deployment health check. Local Windows startup still uses `python app.py`.

The existing service domain is https://app-426bdcf934426d19.up.railway.app/.

For notes to survive redeploys, attach a Railway volume to this service (for example at `/data`). The app automatically stores `notes.db` in `RAILWAY_VOLUME_MOUNT_PATH` when present. You can also override the full file path using `DATABASE_PATH`. Without a volume, the app works but notes can be lost on redeployment.

The deployed app is a shared notes demo: anyone visiting it can see, add, and delete notes.
