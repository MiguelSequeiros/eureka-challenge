# Running the project
Be sure you have docker-compose installed on your local machine to run the project the fastest way.
```
docker-compose up -d
```
### Running the migrations
```
docker-compose run django python stock_service/manage.py migrate
```
### Create a superuser
```
docker-compose run django python stock_service/manage.py createsuperuser
```
# About the solution
- I've decided to use django+django-rest-framework as they provide many built-in features that speed up the 
development.
- For example for the authentication I've used the dj_rest_auth package. I've configured it to provide the API users an access_token and a refresh_token.
- That package also provide us the endpoints to login, logout, register, reset password, etc.
- To expose api_docs I've provided the drf-yasg package. It has an easy configuration and it provides a nice UI to test the endpoints. Anyway, I'm attaching a postman collection to test the main endpoint.
- The throttling can be easily configured in the settings.py file. I've set it to 10 requests per minute per authenticated user. This is thanks to Django REST Framework throttling.

# Steps to test the solution 1 (retrieve stock info)
1. Register a new user
2. Login with the new user and grab the token
3. Use the token to access the stock-info endpoint

# Steps to test the solution 2 (see request_logs)
1. Create a superuser
2. Login with the superuser in the admin panel
3. Go to the request_logs section
