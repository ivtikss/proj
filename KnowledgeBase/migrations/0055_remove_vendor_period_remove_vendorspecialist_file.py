# Generated by Django 4.2.2 on 2023-09-12 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0054_rename_guide_type_certification_typecertification_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='period',
        ),
        migrations.RemoveField(
            model_name='vendorspecialist',
            name='file',
        ),
    ]
