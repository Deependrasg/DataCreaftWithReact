DataCraft

	DataCraft is a web application that users can create and publish and manage data.

Getting Started

	To work on the sample code, you'll need to clone project's repository to your local computer. If you haven't, do that first.

	bitbucket repo : git@bitbucket.org:NitinKadam/datacraft.git

	git clone

	1)Create a Python virtual environment for your Django project. This virtual environment allows you to isolate this project and install any packages you need without affecting the system Python installation. At the terminal, type the following command:

		$ virtualenv -p python3.6 venv

	2)Activate the virtual environment:

		$ source venv/bin/activate

	3)Install Python dependencies for this project:

		$ pip install -r requirements.txt

	4)For Database schema:

		$ python manage.py migrate

	5)Create Super User

		$ python manage.py createsupersuer

	6)Start the Django development server:

		$ python manage.py runserver

Open http://127.0.0.1:8000/ in a web browser to view your application.

What's Here

This sample includes:

README.md - this file

DataCraft/ - this directory contains your Django project files

DataSearch/ - this directory contains your Django application files

manage.py - this Python script is used to start your Django web application

static/ - this directory contains static web assets used by your application

templates/ - this directory contains templates used by your application
