# Generated by Django 2.1.7 on 2019-04-13 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_employeedb_userext'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedb',
            name='userext',
        ),
    ]
