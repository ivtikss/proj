# Generated by Django 4.2.2 on 2023-09-17 08:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0060_alter_vendorspecialist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='KnowledgeBase.questionfaq'),
        ),
        migrations.AlterField(
            model_name='questionfaq',
            name='group',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='KnowledgeBase.groupfaq'),
        ),
        migrations.AlterField(
            model_name='vendorspecialist',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=''),
        ),
    ]
