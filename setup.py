import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='commons',
    version='0.0.1a1',
    packages=find_packages(),
    include_package_data=True,
    license='commons License',
    description='A library for commons',
    long_description=README,
    url='https://github.com/kalumewakitsao/commons',
    author='commons',
    author_email='info@iando.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIKAKI License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        'dj-database-url',
        'Django>=4.0',
        'ipython',
        'djangorestframework',
        'django-extensions',
        'django-filter',
        'psycopg2-binary',

        # celery
        'Celery',
        # celery results
        'django-celery-results',

        'pyyaml',
    ],
    python_requires='>=3.7',
)
