# 📚 Smart Study Planner API

## 📌 Overview

The Smart Study Planner API is a Flask-based application that allows users to track and manage their study sessions.

Users can:

- Add new study sessions
- View all recorded sessions
- Receive a recommendation on which subject to study more

This project demonstrates the use of:

- Flask (API development)
- MySQL (database management)
- Requests (client-side interaction)

---

# ⚙️ Running the Project

## 1. Activate the Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Configuration

Create a file called `config.py` using the template below:

```python
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "yourpassword",
    "database": "study_planner"
}
```

## ⚠️ Important

- Replace the values with your own MySQL credentials
- Do **NOT** commit `config.py`
- `.gitignore` is configured to ignore sensitive files

---

# 🗄️ Database Setup

Run the setup script:

```bash
python setup_db.py
```

This script will:

- Create the database `study_planner`
- Create the table `study_sessions`

---

# 🚀 Running the API

Start the Flask server:

```bash
python app.py
```

Expected output:

```text
Running on http://127.0.0.1:5000/
```

---

# ▶️ Running the Client Simulation

Open a new terminal and run:

```bash
python main.py
```

This simulates a user interacting with the API by:

- Adding study sessions
- Viewing all sessions
- Receiving a study recommendation

---

# 🔌 API Endpoints

## `GET /`

Checks if the API is running.

---

## `GET /sessions`

Returns all study sessions stored in the database.

---

## `POST /sessions`

Adds a new study session.

### Example JSON

```json
{
  "subject": "Math",
  "duration": 60,
  "difficulty": 3,
  "date": "2026-05-04"
}
```

---

## `GET /recommend`

Returns a recommendation for which subject should be studied more.

---

# 🧪 Example Output

```text
SMART STUDY PLANNER

API is running successfully!

Adding study sessions...

All Study Sessions:
ID: 1
Subject: Math
Duration: 60 mins
Difficulty: 3
Date: 2026-05-04

Study Recommendation:
You should study more: Math
```

---

# 📂 Project Structure

```text
Assignment-4-APIs/

─ app.py              # Flask API and endpoints
─ db_utils.py         # Database helper functions
─ setup_db.py         # Database setup script
─ main.py             # Client-side simulation
─ requirements.txt    # Project dependencies
─ .gitignore
─ README.md
```

---

# 🧠 Features

- RESTful API built with Flask
- MySQL database integration
- Client-server interaction using Requests
- Recommendation system based on study frequency
- Input validation and exception handling
- Structured and readable terminal output

---

# 📌 Notes

- Ensure MySQL is running before starting the application
- Update `config.py` before running the project
- Run `app.py` before running `main.py`