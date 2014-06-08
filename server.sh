export DJANGO_SETTINGS_MODULE='raspberrybot.settings'
./bin/django-admin.py videoserver 0.0.0.0:8090 &
videoserver_pid=$!
./bin/django-admin.py runserver 0.0.0.0:8000

kill $videoserver_pid 2>/dev/null
