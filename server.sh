mjpg_streamer -i "input_uvc.so -y -q 95 -f 15 -d /dev/video0" -o "output_http.so -p 8090" &
ms_pid=$!

export DJANGO_SETTINGS_MODULE='raspberrybot.settings'
./bin/django-admin.py runserver 0.0.0.0:8000

kill $ms_pid 2>/dev/null
