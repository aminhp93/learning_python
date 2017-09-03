### Learning Python Site

Note before running these instructions:

- On Ubuntu setup enviroment is python2.7 because mysqlclient is not working on python3. On MacOS is ok for both version.

- Check database.sql file, if it does not have "CREATE DATABASE IF NOT EXISTS 'database_name';" create one before import to MySQL Workbench

- In the settings.py("src/learning_python/settings/py") alter USER and PASSWORD by your local setup.

Instructions:

- clone the project

- cd learning_python

- virtualenv venv

- source venv/bin/activate

- pip install -r requirements.txt

- cd src

- python manage.py runserver

==========================================================================

Next Step:


- Pagedown

- Codemirror

5. Multi language
6. Docker, pusher, notification

http://www.pwc.com/vn/hackaday2017

Reverse engineering (Reserve software, unpack…)
Web (Analyse and exploit vulnerabilities on web services and program logic: SQL injection, XSS, Seasion Hijacking...).
Pwnable (Exploit software).
MISC (Forensic, ACM, Recon,…)