# Generated by Django 5.1.4 on 2025-01-05 20:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0002_marklisttable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetableentry',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administrator.teacher'),
        ),
    ]
