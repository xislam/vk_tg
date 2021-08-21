from django.db import models


class User(models.Model):
    name = models.CharField(max_length=225, verbose_name="Уникальная Имя")

    def __str__(self):
        return self.name
