# Generated by Django 4.2.2 on 2023-09-02 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KnowledgeBase', '0035_remove_product_contact_face'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vendorpartnerspecialist',
            old_name='vendor_partner',
            new_name='vendor',
        ),
    ]