RaspberryBot (0.1.0)
====================
A Simple Robot utilising a RaspberryPi and Raspirobot Board.

.. contents::

Development
-----------

Setup Development Environment::

    $ git clone git@github.com:qoda/raspberrybot.git
    $ cd raspberrybot
    $ virtualenv .
    $ . bin/activate

    # install the requirements
    (bushlog)$ pip install -r requirements.pip

    # running the tests
    (bushlog)$ ./manage.py test

    # running the server
    (bushlog)$ ./manage.py runserver
