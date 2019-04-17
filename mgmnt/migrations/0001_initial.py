# Generated by Django 2.1.7 on 2019-04-04 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='aaauserdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('usern', models.CharField(max_length=30)),
                ('passw', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alertsdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alerttype', models.CharField(max_length=15)),
                ('alertstatus', models.CharField(default='active', max_length=10)),
                ('alertmsg', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orginfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Solve The Network', max_length=100)),
                ('address', models.TextField(default='')),
                ('phnum', models.IntegerField(default=0)),
                ('emailid', models.CharField(default='info@solvethenetwork.com', max_length=100)),
                ('orgurl', models.URLField(default='https://solvethenetwork.com')),
                ('chkinfo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='userextension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=30)),
                ('website', models.URLField(default='')),
                ('phone', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='profile_image')),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]