# Generated by Django 4.2.2 on 2023-09-19 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0068_alter_answer_options_alter_groupfaq_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='files',
        ),
    ]