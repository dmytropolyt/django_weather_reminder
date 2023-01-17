# django_weather_reminder 
--
Service of weather notification in the subscribed city via email

Django_wheather_remider application is provided API for getting information about the weather.

User can register and get auth token like a JWT (JSON web token). The user can subscribe/unsubscribe to one or a few cities with parameters like a period of notification(1, 3, 6, 12 hours), etc. The user can edit parameters of subscribing or delete. The user can get a list of subscribing.

It uses third-party service for getting actual weather data.

Application sends notifications via an email by Celery, Celery-beat and Redis.

Stack:
--
+ Backend: Python(Django, Django Rest Framework)
+ Database: PostgreSQL
+ Virtualization: Docker
+ Background Task Queue: Celery
+ Broker: Redis