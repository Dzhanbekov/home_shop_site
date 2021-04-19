# Generated by Django 3.2 on 2021-04-19 19:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('address', models.CharField(max_length=110, verbose_name='Адрес')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('region', models.CharField(max_length=100, verbose_name='Область')),
                ('zipcode', models.CharField(max_length=20, verbose_name='Индекс')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('bedrooms', models.IntegerField(verbose_name='спальная комната')),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='ванная комната')),
                ('garage', models.IntegerField(default=0, verbose_name='Гараж')),
                ('sqmt', models.IntegerField(verbose_name='Квадрат метров')),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Размер лота')),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Главное фото')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото1')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото2')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото3')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото4')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото5')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото6')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='дата')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor', verbose_name='Реалтор')),
            ],
        ),
    ]
