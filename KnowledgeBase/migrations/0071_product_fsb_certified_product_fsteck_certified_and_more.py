# Generated by Django 4.2.2 on 2023-10-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0070_alter_answer_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fsb_certified',
            field=models.BooleanField(default=False, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='fsteck_certified',
            field=models.BooleanField(default=False, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='top_certified',
            field=models.BooleanField(default=False, max_length=50, null=True),
        ),
    ]