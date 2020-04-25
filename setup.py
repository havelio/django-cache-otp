import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django_otp_cache',
    version='v0.1',
    packages=['django_otp_cache'],
    description='one time password based on django cache',
    long_description=README,
    author='havelio',
    author_email='havelioh@gmail.com',
    url='https://github.com/havelio/django-otp-cache/',
    license='MIT',
    install_requires=[
        'Django>=2',
    ]
)
