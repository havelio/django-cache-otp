import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='django_cache_otp',
    version='v0.1',
    packages=['django_cache_otp'],
    description='one time password based on django cache',
    long_description=README,
    author='havelio',
    author_email='havelioh@gmail.com',
    url='https://github.com/havelio/django-cache-otp/',
    license='MIT',
    install_requires=[
        'Django>=2',
    ]
)
