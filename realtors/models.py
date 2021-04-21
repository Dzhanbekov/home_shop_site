from django.db import models
from datetime import datetime


class Realtor(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.CharField(max_length=50,)
    is_mvp = models.BooleanField(default=False, verbose_name='Работник месяца')
    hire_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='дата приема на работу')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Риелтор'
        verbose_name_plural = 'Риелторы'