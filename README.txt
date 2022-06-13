# Quiz-App

First you need to run following commands to install required packages
pip install Django
pip install djangorestframework
pip install django-cors-headers 
pip install django-rest-framework

Second you have to run commands in the current directory
python manage.py makemigrations
python manage.py makemigrate
python manage.py runserver

After that your server will be ready and then whatever your localhost will be you can check the functionality by putting '/admin' in the URL.
To use the /admin you should create the super user for that you have to run following command: 'python manage.py createsuperuser' then it'll ask 
an email and password, you can enter the email and password of your choice and you can use thus super user in Django admin.

And you can also check these API's throught the postman. For that you have to import the .json collection file (given in the repository) into your postman app.

You have first sign up/log in and then you can use that generated token everywhere.

