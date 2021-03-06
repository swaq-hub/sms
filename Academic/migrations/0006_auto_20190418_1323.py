# Generated by Django 2.2 on 2019-04-18 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_auto_20190413_1455'),
        ('Academic', '0005_subjects_periodnumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='classno',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='periodnumber',
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='teacher',
        ),
        migrations.CreateModel(
            name='subjectallocat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.Classes')),
                ('periodnumber', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Academic.Periods')),
                ('subjectid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Academic.Subjects')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.employeeDB')),
            ],
        ),
        migrations.CreateModel(
            name='examsschedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.DateTimeField()),
                ('subjectid', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Academic.Subjects')),
            ],
        ),
    ]
