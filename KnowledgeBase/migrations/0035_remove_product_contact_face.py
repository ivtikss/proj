# Generated by Django 4.2.2 on 2023-07-17 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0034_rename_id_вендора_product_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='contact_face',
        ),
    ]