# Generated by Django 5.1.4 on 2024-12-18 22:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_facultytable_logintable_notificationtable_timetable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studenttable',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administrator.logintable'),
            preserve_default=False,
        ),
    ]
