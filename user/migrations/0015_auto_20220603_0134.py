# Generated by Django 3.2.13 on 2022-06-03 01:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20220603_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='code',
            field=models.CharField(default='a=m=wQkX*g5vO6DG3.b5!7WO4anK$qCTcLUEw&Jb,Chl*c?B7MzP<&TTitYNJ1XTkHHHsza1BQW>yw!uC#!hU96KuR.v.4B', max_length=128),
        ),
        migrations.AlterField(
            model_name='otpmodel',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 1, 39, 1, 744199, tzinfo=utc)),
        ),
    ]