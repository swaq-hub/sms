# Generated by Django 2.1.7 on 2019-04-13 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mgmnt', '0005_auto_20190413_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userextension',
            name='image',
        ),
    ]
