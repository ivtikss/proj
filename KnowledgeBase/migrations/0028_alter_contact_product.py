# Generated by Django 4.2.2 on 2023-07-14 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0027_alter_product_id_вендора'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='KnowledgeBase.vendor'),
        ),
    ]