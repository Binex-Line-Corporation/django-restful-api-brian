# django-restful-api-brian
Practice project to make a RESTful API server using django.


# Setup Guide
#### The following sections are a step-by-step guide for the setup of this API server on a Windows machine:

## Start Django Project
1. Install [Python](https://www.python.org/downloads/). At time of writing, Python 3.9.6.
2. Navigate to the project folder in a terminal, create a virtual environment, and activate it.

   ```
   PS C:\Users\Brian Choi\Documents\Projects\API\django-restful-api-brian> python -m venv venv
   PS C:\...\django-restful-api-brian> .\venv\Scripts\activate
   ```

3. Install Django and the REST API framework for Django.

   ```
   PS C:\...\django-restful-api-brian> pip install django
   PS C:\...\django-restful-api-brian> pip install djangorestframework
   ```
   
4. Start the Django project using the django-admin.py script. Here, "rest_api" is the project name.

   ```
   PS C:\...\django-restful-api-brian> django-admin startproject rest_api
   ```
   
5. Add "rest_framework" in the list of installed apps in settings.py.

   ``` Python
   INSTALLED_APPS = [
      'django.contrib.admin',
      ...
      'rest_framework',
   ]
   ```
   
   
## Setup MySQL DB
1. Install [MariaDB Server](https://mariadb.org/download/). At time of writing, MariaDB Server 10.6.4. During setup, take note of the root password and port number.
2. Open the HeidiSQL application that got installed along with MariaDB and use the root password mentioned above to open a connection to the MariaDB server.
3. Create a new database in the server and take note of the database name. The name will be used to identify the database in the settings.py file.

## Use MySQL DB in Django Project
1. Edit the default dictionary in the DATABASES dictionary in settings.py to have the following entries:

   ``` Python
   DATABASES = {
      'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': '[enter the name of the database created in step 3 above]',
         'USER': 'root',
         'PASSWORD': '[enter the root password from step 1 above]',
         'PORT': '[should be 3306 if you did not change port number]',
      }
   }
   ```
   
2. Create a new folder called "stocks" (name can be anything) in the top level of the project directory. This will house the API and the models for the database.
3. Add the "stocks" in the list of installed apps in settings.py.

   ``` Python
   INSTALLED_APPS = [
      'django.contrib.admin',
      ...
      'stocks', # This is the name of the API application in this repo
   ]
   ```

4. Create a new file named models.py in the stocks folder and create a table for the database.

   ``` Python
   from django.db import models

   # Create your models here.

   class stocks(models.Model):
      ticker = models.CharField(max_length=4)
      company_name = models.CharField(max_length=100)
      date = models.DateField()
      opening_price = models.FloatField()
      closing_price = models.FloatField()
   ```
   
5. Through the terminal, generate the migration code to update the database and then apply the migration.

   ```
   PS C:\...\django-restful-api-brian> python .\rest_api\manage.py makemigrations stocks
   PS C:\...\django-restful-api-brian> python .\rest_api\manage.py migrate stocks
   ```
