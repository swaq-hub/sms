# Generated by Django 2.1.7 on 2019-04-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_auto_20190414_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsdb',
            name='simage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
