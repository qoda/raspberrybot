RaspberryBot (0.1.0)
====================
A Simple WiFi Controlled RaspberryPi Robot.

.. contents::

Development
-----------

Setup Development Environment::

    $ git clone git@github.com:qoda/raspberrybot.git
    $ cd raspberrybot
    $ virtualenv .
    $ . bin/activate

    # install the requirements
    (raspberrybot)$ pip install -r requirements.pip

    # running the tests
    (raspberrybot)$ ./manage.py test

    # running the server
    (raspberrybot)$ ./manage.py runserver
