# Examen-Volindo-django

Requirements

    You will need to have a version of python 3 installed.

check this by using the following command

Create a virtual environment and activate it using the following commands:

python3 -m venv venv
source venv/bin/activate

Once you've activated your virtual environment install your python packages by running:

pip install -r requirements.txt

The project was configured in Postgres so we must be have postgres run with the next configuration 

   'NAME': 'django_tasks',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST':'localhost',
        'PORT':''
        
python manage.py migrate

python manage.py runserver
        
