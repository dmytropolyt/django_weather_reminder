from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'


class Subscribe(models.Model):
    class Parameter(models.IntegerChoices):
        ONE = 1
        THREE = 3
        SIX = 6
        TWELVE = 12

    city = models.ForeignKey(City, to_field='name', on_delete=models.CASCADE)
    user = models.ForeignKey(User, to_field='username', related_name='subscribes', on_delete=models.CASCADE)
    parameter = models.IntegerField(choices=Parameter.choices, default=Parameter.THREE)

    def __str__(self):
        return f'{self.city}, {self.user}'
