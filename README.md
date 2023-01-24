# Django PostgreSQL React

## Purpose
This project is build to learn about the intergration of these three technologies: Django, PostgreSQL, and React.

## Installation

* Install python 3, PostgreSQL, and Node.js from their sites and set them up.  
* Create a directory for this project and cd into that directory in the command line.  This folder directory will only hold the project and invironment files.
* Create a virtual environment for the project by typing, python -m venv env, into the command line
* login to the virtual environment by typing, env\Scripts\activate, into the command line (windows only)
* Install python packages: pip install django djangorestframework django-cors-headers psycopg2 python-decouple
* cd to client 
* install node packages: npm i

## Database
* login to with default user PostgreSQL: psql -U postgres
* create database in postgres=# command line: CREATE DATABASE test;
* python manage.py makemigrations
* python manage.py migrate