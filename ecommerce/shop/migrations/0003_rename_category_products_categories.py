# Generated by Django 5.1.2 on 2024-10-29 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category',
            new_name='categories',
        ),
    ]
