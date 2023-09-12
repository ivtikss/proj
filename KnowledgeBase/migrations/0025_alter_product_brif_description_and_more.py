# Generated by Django 4.2.2 on 2023-07-14 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0024_remove_vendorpartner_specialist_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brif_description',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='gen_form',
            field=models.FileField(default=None, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='owner_type',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='ship_kit',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tech_support',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='top',
            field=models.BooleanField(default=False, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='whom_and_what_for',
            field=models.TextField(default='', null=True),
        ),
    ]
