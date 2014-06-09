from setuptools import setup, find_packages
from setuptools.command import sdist

del sdist.finders[:]

setup(

    # project description
    name='raspberrybot',
    version='0.2.0',
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
        'raspirobotboard==1.0',
        'numpy==1.8.1',
        'PIL==1.1.7',
        'scipy==0.10.1',
        'pygame==1.9.1release',
        'SimpleCV==1.3'
    ],
    scripts=[
        'server.sh'
    ]
)
