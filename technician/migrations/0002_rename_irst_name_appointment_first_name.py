# Generated by Django 5.1.2 on 2024-10-09 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technician', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='irst_name',
            new_name='first_name',
        ),
    ]
