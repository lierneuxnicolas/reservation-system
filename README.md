📌 Reservation System
🔹 Introduction

Application web développée avec Django (Python) permettant de gérer :

des utilisateurs
un catalogue
des réservations

Projet réalisé dans le cadre d’un apprentissage du développement web backend.

⚙️ Installation (Mode opératoire)
Prérequis
Python 3.10+
pip
Étapes
git clone https://github.com/lierneuxnicolas/reservation-system.git
cd reservation-system
python -m venv .venv
.venv\Scripts\Activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Accès
http://127.0.0.1:8000/
(Optionnel) Admin
python manage.py createsuperuser
http://127.0.0.1:8000/admin
✅ Résumé rapide
Backend : Django (Python)
DB : SQLite
Lancement : runserver
Toujours activer .venv
