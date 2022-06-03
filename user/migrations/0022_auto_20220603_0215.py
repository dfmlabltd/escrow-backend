# Generated by Django 3.2.13 on 2022-06-03 02:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0021_auto_20220603_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='code',
            field=models.CharField(default='3Mkn1CnSy1U6$Zq5H0XkTBk6.9tUPGUwM1$4#I8iqhCzvFhnHwopq69^_b,u>_kQ4X9jn?wI<.O5,ebKOR3Ndj<QfHUWTq)^cbGvygZGR,RiddR1_ho,', max_length=128),
        ),
        migrations.AlterField(
            model_name='otpmodel',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 2, 20, 15, 843373, tzinfo=utc)),
        ),
    ]
