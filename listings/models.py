from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING, verbose_name='Реалтор')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    address = models.CharField(max_length=110, verbose_name='Адрес')
    city = models.CharField(max_length=100, verbose_name='Город')
    region = models.CharField(max_length=100, verbose_name='Область')
    zipcode = models.CharField(max_length=20, verbose_name='Индекс')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    bedrooms = models.IntegerField(verbose_name='спальная комната')
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1, verbose_name='ванная комната')
    garage = models.IntegerField(default=0, verbose_name='Гараж')
    sqmt = models.IntegerField(verbose_name='Квадрат метров')
    lot_size = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Размер лота')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='фото1')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='фото2')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='фото3')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='фото4')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='фото5')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='фото6')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    list_date = models.DateTimeField(default=datetime.now, blank=True, verbose_name='дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список'
        verbose_name_plural = 'Списки'