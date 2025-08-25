MediMate - Personal Health and Medicine Tracker
==============================================
MediMate is a Django-based web application that helps users track their medicines, appointments, vitals (like blood pressure, sugar level, and weight), and view interactive health graphs.

🚀 Features
-----------

✅ User authentication (Signup/Login/Logout)

✅ Profile management with DOB and emergency contact

✅ Add/Edit/Delete:

Medicines with schedule tracking

Appointments with doctors

Vitals data (BP, Sugar, Weight)

📊 Vitals graph visualization using Chart.js

📱 Mobile-responsive Bootstrap 5 UI

⚙️ Tech Stack
-------------
Backend: Django 5.x

Database: SQLite (default)

Frontend: Bootstrap 5, Chart.js

Hosting: Render

🛠️ Setup Instructions (Local)
-----------------------------
Clone the repository:

git clone https://github.com/harsh12314/medimate.git


Navigate to the project:

cd medimate


Create virtual environment:

python -m venv env
source env/bin/activate     # Linux/macOS
env\Scripts\activate        # Windows


Install dependencies:

pip install -r requirements.txt


Create .env file (optional – for email support):

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_password


Apply migrations:

python manage.py makemigrations
python manage.py migrate


Run the server:

python manage.py runserver

🌐 Deployment Notes (Render)

Add your Render project domain in settings.py under:

CSRF_TRUSTED_ORIGINS = [
    "https://your-app-name.onrender.com",
]
ALLOWED_HOSTS = ['your-app-name.onrender.com', '127.0.0.1', 'localhost']


In Render Dashboard, set build & start commands:

Build command: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
Start command: gunicorn medimate.wsgi


Set environment variables (like EMAIL_HOST_USER, EMAIL_HOST_PASSWORD) in Render Environment if needed.

👨‍💻 Author
==========
T. Harsh Vardhan Singh
📧 Contact: thvs.166@gmail.com
