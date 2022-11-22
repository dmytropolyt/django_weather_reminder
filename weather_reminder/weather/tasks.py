from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from celery import shared_task
from .models import Subscribe
from .funcs import add_weather_info


@shared_task(name='weather_reminder.tasks.send_mail_1_hour')
def send_mail_1_hour():
    users = Subscribe.objects.filter(parameter=1).all()
    for user in users:
        print('Mail sending...')
        data = add_weather_info(str(user.city))

        message = f"{data['name']} \n Temperature - {data['temperature']} \n Feels like - {data['feels_like']} \n " \
                  f"Country - {data['country_code']} \n Description - {data['description']} \n" \
                  f"Wind speed - {data['wind_speed']} \n Pressure - {data['pressure']} \n " \
                  f"Humidity - {data['humidity']} \n Visibility - {data['visibility']}"
        email_to = User.objects.filter(username=user.user).first().email

        send_mail(
            subject='WeatherReminder',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_to],
            fail_silently=True
        )
    return "Mail has been sent"


@shared_task(name='weather_reminder.tasks.send_mail_3_hours')
def send_mail_3_hours():
    users = Subscribe.objects.filter(parameter=3).all()
    for user in users:
        print('Mail sending...')
        data = add_weather_info(str(user.city))

        message = f"{data['name']} \n Temperature - {data['temperature']} \n Feels like - {data['feels_like']} \n " \
                  f"Country - {data['country_code']} \n Description - {data['description']} \n" \
                  f"Wind speed - {data['wind_speed']} \n Pressure - {data['pressure']} \n " \
                  f"Humidity - {data['humidity']} \n Visibility - {data['visibility']}"
        email_to = User.objects.filter(username=user.user).first().email

        send_mail(
            subject='WeatherReminder',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_to],
            fail_silently=True
        )
    return "Mail has been sent"


@shared_task(name='weather_reminder.tasks.send_mail_6_hours')
def send_mail_6_hours():
    users = Subscribe.objects.filter(parameter=6).all()
    for user in users:
        print('Mail sending...')
        data = add_weather_info(str(user.city))

        message = f"{data['name']} \n Temperature - {data['temperature']} \n Feels like - {data['feels_like']} \n " \
                  f"Country - {data['country_code']} \n Description - {data['description']} \n" \
                  f"Wind speed - {data['wind_speed']} \n Pressure - {data['pressure']} \n " \
                  f"Humidity - {data['humidity']} \n Visibility - {data['visibility']}"
        email_to = User.objects.filter(username=user.user).first().email

        send_mail(
            subject='WeatherReminder',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_to],
            fail_silently=True
        )
    return "Mail has been sent"


@shared_task(name='weather_reminder.tasks.send_mail_12_hours')
def send_mail_12_hours():
    users = Subscribe.objects.filter(parameter=12).all()
    for user in users:
        print('Mail sending...')
        data = add_weather_info(str(user.city))

        message = f"{data['name']} \n Temperature - {data['temperature']} \n Feels like - {data['feels_like']} \n " \
                  f"Country - {data['country_code']} \n Description - {data['description']} \n" \
                  f"Wind speed - {data['wind_speed']} \n Pressure - {data['pressure']} \n " \
                  f"Humidity - {data['humidity']} \n Visibility - {data['visibility']}"
        email_to = User.objects.filter(username=user.user).first().email

        send_mail(
            subject='WeatherReminder',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_to],
            fail_silently=True
        )
    return "Mail has been sent"
