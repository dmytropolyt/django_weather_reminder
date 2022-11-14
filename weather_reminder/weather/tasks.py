from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from .models import Subscribe
from .funcs import add_weather_info


@shared_task(name='Send weather every hour')
def send_mail_1_hour():
    users = Subscribe.objects.filter(parameter=1).all()
    for user in users:
        print('Mail sending...')
        data = add_weather_info(str(user.city))
        #mail_subject = 'WeatherReminder'
        message = f"{data['name']} \n {data['temperature']} \n {data['feels_like']} \n {data['country_code']} \n" \
                  f"{data['description']} \n {data['wind_speed']} \n {data['pressure']} \n {data['humidity']} \n " \
                  f"{data['visibility']}"
        email_to = User.objects.filter(username=user.username).first().email

        send_mail(
            subject='WeatherReminder',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email_to],
            fail_silently=False
        )
    return "Mail has been sent"


@shared_task(name='Send weather every 3 hours')
def send_mail_3_hour():
    return "Mail has been sent"


@shared_task(name='Send weather every 6 hours')
def send_mail_6_hour():
    return "Mail has been sent"


@shared_task(name='Send weather every 12 hours')
def send_mail_12_hour():
    return "Mail has been sent"
