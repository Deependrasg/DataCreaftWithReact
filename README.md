DataCraft

	DataCraft is a web application that users can create and publish and manage data.

Getting Started

	To work on the sample code, you'll need to clone project's repository to your local computer. If you haven't, do that first.

	bitbucket repo :

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

	7)Compress All CSS and JS files
	    $ python manage.py compress

Open http://127.0.0.1:8000/ in a web browser to view your application.

Install postgres and configure.

		a)Install postgres
		 	sudo apt-get install postgresql postgresql-contrib
		b)Create DB and user
			# sudo -i -u postgres
			# psql
			postgres=# create user data with password 'Temp1234';
			postgres=# create database datacraft owner data;
			postgres=# \l (show all database)
			postgres=# \c datacraft (use database)
			postgres=# alter user data superuser createrole createdb replication;

After configure Databse create .env file inside DataCraft (Its django project folder
        its contains with settings.py,wsgi.py or etc) folder

        add this credential:

	        DATABASE_NAME='datacraft'
			DATABASE_USERNAME='data'
			DATABASE_PASSWORD='Temp1234'
			EMAIL_HOST_USER='Your email'
			EMAIL_HOST_PASSWORD='Your email password'


Save .env file then run this commnad on terminal
       $ source .env


Install Elastic Search
       $ mkdir elasticsearch
       $ cd elasticsearch
       $ wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.1.1.tar.gz
       $ tar -xzf elasticsearch-5.1.1.tar.gz
       $ ./elasticsearch-5.1.1/bin/elasticsearch -d

    Test Elastic Search

    	$ curl -XGET http://localhost:9200

    	OutPut:
    			{
				  "name" : "XsC6IwR",
				  "cluster_name" : "elasticsearch",
				  "cluster_uuid" : "B7VmwwuHTTKDIO9W6l66iw",
				  "version" : {
				    "number" : "5.1.1",
				    "build_hash" : "5395e21",
				    "build_date" : "2016-12-06T12:36:15.409Z",
				    "build_snapshot" : false,
				    "lucene_version" : "6.3.0"
				  },
				  "tagline" : "You Know, for Search"
				}


Run Celery in Background in both side AWS and Private server:

		celery -A DataCraft worker -l info &

What's Here

This sample includes:

README.md - this file

DataCraft/ - this directory contains your Django project files

DataSearch/ - this directory contains your Django application files

manage.py - this Python script is used to start your Django web application

static/ - this directory contains static web assets used by your application

templates/ - this directory contains templates used by your application


For the FrontEnd application:

1) Open react
2) npm install
3) npm start
