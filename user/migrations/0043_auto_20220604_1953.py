# Generated by Django 3.2.13 on 2022-06-04 19:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0042_auto_20220604_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='code',
            field=models.CharField(default='?OAxysIzPD4e!?Lq0#ycHuItUb7dfL&R1or)YnYsFshj%Ysx.XZIl#E(I0nK6y^DVm*)Z69ZivANfsE3^aXb4TQ_9XFab', max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='otpmodel',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 19, 58, 30, 554059, tzinfo=utc)),
        ),
    ]