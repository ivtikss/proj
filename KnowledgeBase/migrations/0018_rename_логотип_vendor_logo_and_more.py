# Generated by Django 4.2.2 on 2023-06-28 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0017_alter_certification_дата_начала_действия_лицензии_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendor',
            old_name='Логотип',
            new_name='logo',
        ),
        migrations.RenameField(
            model_name='vendor',
            old_name='Название Вендора',
            new_name='name',
        ),
    ]
