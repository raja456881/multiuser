# Generated by Django 3.0.7 on 2020-09-25 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20200925_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 25, 18, 14, 15, 666781)),
        ),
    ]
