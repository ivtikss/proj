# Generated by Django 4.2.2 on 2023-09-18 16:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0065_alter_vendorspecialist_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorspecialist',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='vendorspecialist',
            name='vendor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='KnowledgeBase.vendor', verbose_name='У какого вендора?'),
        ),
    ]
