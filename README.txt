
MediMate - Personal Health and Medicine Tracker
==============================================

MediMate is a Django-based web application that helps users track their medicines, appointments, vitals (like blood pressure, sugar level, and weight), and generate health graphs.

Features
--------
- User authentication (Signup/Login/Logout)
- Profile management with DOB and emergency contact
- Add/Edit/Delete:
  - Medicines with schedule tracking
  - Appointments with doctors
  - Vitals data (BP, Sugar, Weight)
- View vitals graph using Chart.js
- Mobile-responsive Bootstrap UI

Tech Stack
----------
- Django 5.x
- SQLite (default)
- Bootstrap 5
- Chart.js
- Railway deployment support

Setup Instructions (Local)
--------------------------
1. Clone the repository:
   git clone https://github.com/harsh12314/medimate.git

2. Navigate to the project:
   cd medimate

3. Create virtual environment:
   python -m venv env
   source env/bin/activate     (Linux/macOS)
   env\Scripts\activate        (Windows)

4. Install dependencies:
   pip install -r requirements.txt

5. Create `.env` file (for email support, optional):
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_password

6. Apply migrations:
   python manage.py makemigrations
   python manage.py migrate

7. Run the server:
   python manage.py runserver

Deployment Notes (Railway)
--------------------------
1. Add your Railway project domain in `settings.py` under:

   CSRF_TRUSTED_ORIGINS = [
       "https://your-app-name.up.railway.app",
   ]
   ALLOWED_HOSTS = ['your-app-name.up.railway.app', '127.0.0.1', 'localhost']

2. In Railway Dashboard, set build & start commands:
   Build command: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
   Start command: gunicorn medimate.wsgi

3. Make sure to set environment variables like `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` on Railway if needed.

Author
------
T. Harsh Vardhan Singh

Contact: thvs.166@gmail.com
