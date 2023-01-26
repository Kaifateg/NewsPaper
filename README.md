# Project name - NewsPaper
This project is a website with news.

# Some functions
## Registration methods:
  1. Email and password.
  2. Yandex account.
  User receives a confirmation email.

## Rights
  Rights are issued through the admin panel.
  Users with appropriate rights can create, edit and delete news.
  
## Alerts
  The website has a follow system for registered users.
  Users receive alerts about created news in the selected category.
  Every Monday at 08:00 am, users receive a list of news for the week in the selected category.
  
# Settings
  Create .env file with your arguments (without quotes):
    1. SECRET_KEY='Django secret key'
    2. EMAIL_HOST_USER='From Yandex email'
      Example: Your email - user1@yandex.ru. Then EMAIL_HOST_USER=user1
    3. EMAIL_HOST_PASSWORD='From Yandex email'
    4. DEFAULT_FROM_EMAIL='Email to send messages (Yandex)'
    5. CELERY_BROKER_URL=''
      Example: CELERY_BROKER_URL=redis://username:password@host:port
      
# Start
  To run periodic tasks on Windows, run in different terminal windows:
    1. celery -A PROJECT worker -l INFO
    2. celery -A PROJECT beat -l INFO
    
  To start a project: python manage.py runserver
