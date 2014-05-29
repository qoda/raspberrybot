RaspberryBot (0.1.6)
====================
A Simple WiFi Controlled RaspberryPi Robot.

.. contents::

Development
-----------

Requirements:

* git
* python-pip
* python-virtualenv

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

Production
-----------

Requirements:

* git
* python-pip
* python-virtualenv
* RPi

Setup Production Environment::

    $ virtualenv .
    $ pip install https://github.com/qoda/raspberrybot.git@0.1.6
    $ . bin/activate

    # running the tests
    (raspberrybot)$ django-admin.py test

    # running the server
    (raspberrybot)$ django-admin.py runserver <ip_adress> <port>
