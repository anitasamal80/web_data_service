# wds-django
Django Project - An authenticated web data service using Django, SQLite and Plotly.

## create a virtual environment
python -m venv .venv

## Activate the virtual environment from a cmd.exe command prompt
.venv\Scripts\activate.bat

## Install & Upgrade pip
python -m pip install --upgrade pip

## Install your dependencies
python -m pip install django

# Check if django has been installed & version
python -m django --version

# Strat a new django project
django-admin startproject mybaseproject

# Go to that project
cd mybaseproject

# To run the django development server
python manage.py runserver
# To stop a server
ctrl+c

# Start a new web app
python manage.py startapp webdataservice

# Created a file urls.py in webdataservice app
# Added a view in views.py within the app
# Added a path in the app/urls.py file within the app
# Added routing to the application paths.
# Created HTML Templates
# Added your webdataservice to INSTALLED_APP list in projects settings.py

# Create a data model class in models.py
# Make Migration scripts
python manage.py makemigrations

# migrate the db (create/update the database tables)
python manage.py migrate

# create a admin user to login to the Admin site
python manage.py createsuperuser

# register the models in admin.py, for example admin.site.register(Model name)

# Added data model to the response in views.py
# Added plotly and pandas dependency for the chart
pip install pandas
pip install plotly

# Created a Line graph using plotly  
# Added data and the plot to html template



