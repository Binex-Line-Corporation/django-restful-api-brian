# django-restful-api-brian
Practice project to make a RESTful API server using django.


#### The following section is a step-by-step guide for the setup of this API server on a Windows machine:
1. Install [Python](https://www.python.org/downloads/).
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
   PS C:\...\django-restful-api-brian> python .\venv\Scripts\django-admin.py startproject rest_api
   ```
   
