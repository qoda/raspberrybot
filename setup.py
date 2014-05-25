from setuptools import setup, find_packages
from setuptools.command import sdist

del sdist.finders[:]

setup(

    # project description
    name='raspberrybot',
    version='0.1.0',
    description='A Simple WiFi Controlled RaspberryPi Robot',
    long_description="%s\n\n%s" % (open('README.rst', 'r').read(), open('AUTHORS.rst', 'r').read()),
    author='Jonathan Bydendyk',
    author_email='jpbydendyk@gmail.com',
    url='https://github.com/qoda/raspberrybot',

    # packaging
    packages=find_packages(),
    include_package_data=True,

    # dependancies
    dependency_links=[
        'git+https://github.com/simonmonk/raspirobotboard.git'
    ],
    install_requires=[
        'Django>=1.6',
        'rpi.gpio==0.5.5',
        'pyserial==2.7',
        'raspirobotboard==1.0'
    ],
    scripts=[]
)
