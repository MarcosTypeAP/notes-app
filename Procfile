release: python manage.py migrate
web: mkdir /media; python manage.py collectstatic --no-input; gunicorn djangoNotesApp.wsgi 
