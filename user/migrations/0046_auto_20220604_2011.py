# Generated by Django 3.2.13 on 2022-06-04 20:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0045_auto_20220604_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='code',
            field=models.CharField(default='Wyy9=6XYW,p.P*Q7_7ClXA9hI<zmK?*r,5inMLVDDV4*q5Wvb#el3b3uwVdIh52JUnmc<KM.<I?q!B$IZv7PH.L#Wp', max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='otpmodel',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 20, 16, 51, 910376, tzinfo=utc)),
        ),
    ]
