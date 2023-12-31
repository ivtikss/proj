# Generated by Django 4.2.2 on 2023-06-22 13:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Название Вендора', models.CharField(default='', max_length=50)),
                ('Логотип', models.ImageField(default=None, upload_to='')),
                ('Партнеры', models.CharField(default='', max_length=50)),
                ('Контакты', models.CharField(default='', max_length=50)),
                ('Цены', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VendorPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Статус', models.CharField(default='', max_length=50)),
                ('Срок действия статуса', models.DateField(default=datetime.datetime(2023, 6, 22, 18, 22, 49, 514342), max_length=50)),
                ('Требования к статусу', models.CharField(default='', max_length=50)),
                ('Список специалтстов', models.CharField(default='', max_length=50)),
                ('id Вендора', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='KnowledgeBase.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorPrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Прайсы', models.FileField(default=None, upload_to='')),
                ('Дата начала действия прайса', models.DateField(default=datetime.datetime(2023, 6, 22, 18, 22, 49, 514342))),
                ('Сертификат', models.FileField(default=None, upload_to='')),
                ('id Вендора', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='KnowledgeBase.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorPartnerSpecialist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Имя специалиста', models.CharField(default='', max_length=50)),
                ('Срок действия сертификата', models.DateField(default=datetime.datetime(2023, 6, 22, 18, 22, 49, 514342), max_length=50)),
                ('Сертификат', models.FileField(upload_to='')),
                ('id блока Партнерства', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='KnowledgeBase.vendorpartner')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Название продукта', models.CharField(default='', max_length=50)),
                ('Топ', models.BooleanField(default=False, max_length=50)),
                ('Краткое описание', models.TextField(default='')),
                ('Кому и для чего', models.TextField(default='')),
                ('Общая анкета ', models.FileField(default=None, upload_to='')),
                ('Комплект отгрузки', models.CharField(default='', max_length=200)),
                ('Техническая поддержка', models.CharField(default='', max_length=200)),
                ('Принцип владения', models.CharField(default='', max_length=100)),
                ('Прайс', models.FileField(default=None, upload_to='')),
                ('Дополнительный комментарий', models.TextField(default='')),
                ('Общая анкета', models.FileField(default=None, upload_to='')),
                ('Тип продукта', models.CharField(default='', max_length=50)),
                ('Компетенции', models.FileField(default=None, upload_to='')),
                ('id Блока <Реализация>', models.CharField(default='', max_length=50)),
                ('id Блока <Лицензирование>', models.CharField(default='', max_length=50)),
                ('id Блока <Варианты отгрузки>', models.CharField(default='', max_length=50)),
                ('id Блока <Сертификация>', models.CharField(default='', max_length=50)),
                ('id Вендора', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='KnowledgeBase.vendor')),
            ],
        ),
    ]
