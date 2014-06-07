mjpg_streamer -i "/usr/lib/input_uvc.so -y -d /dev/video0" -o "/usr/lib/output_http.so -p 8090" &
ms_pid=$!

export DJANGO_SETTINGS_MODULE='raspberrybot.settings'
./bin/django-admin.py runserver 0.0.0.0:8000

kill $ms_pid 2>/dev/null
