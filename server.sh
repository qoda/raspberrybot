mjpg_streamer -i "/usr/lib/input_uvc.so -y -d /dev/video0" -o "/usr/lib/output_http.so -p 8090"
export DJANGO_SETTINGS_MODULE='raspberrybot.settings'
./bin/django-admin.py runserver 10.0.0.7:8000
