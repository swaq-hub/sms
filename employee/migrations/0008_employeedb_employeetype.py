# Generated by Django 2.1.7 on 2019-04-13 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_employeedb_userext'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedb',
            name='employeetype',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='employee.Employeetype'),
            preserve_default=False,
        ),
    ]
