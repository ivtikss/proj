# Generated by Django 4.2.2 on 2023-06-27 06:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0016_alter_certification_дата_начала_действия_лицензии_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='Дата начала действия лицензии',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='infodeal',
            name='Дата начала действия лицензии',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='licence',
            name='Дата начала действия лицензии',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vendorpartner',
            name='Срок действия статуса',
            field=models.DateField(default=django.utils.timezone.now, max_length=50),
        ),
        migrations.AlterField(
            model_name='vendorpartnerspecialist',
            name='Срок действия сертификата',
            field=models.DateField(default=django.utils.timezone.now, max_length=50),
        ),
        migrations.AlterField(
            model_name='vendorprices',
            name='Дата начала действия прайса',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
