📌 Reservation System
🔹 Description

This project is a web application built with Django (Python).
It allows users to manage accounts, browse a catalogue, and handle reservations.

It was developed as part of a learning project to understand backend development and web application structure.

🛠️ Technologies
Backend: Django (Python)
Database: SQLite
Frontend: HTML (Django templates)
Tools: Git, GitHub, VS Code
⚙️ Installation
Prerequisites
Python 3.10+
pip
Setup
git clone https://github.com/lierneuxnicolas/reservation-system.git
cd reservation-system
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
🚀 Usage

Open your browser and go to:

http://127.0.0.1:8000/
🔐 Admin (optional)
python manage.py createsuperuser

Then access:

http://127.0.0.1:8000/admin
✅ Summary
Django-based web application
User management + catalogue + reservations
Easy local setup with virtual environment
