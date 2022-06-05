# Generated by Django 3.2.13 on 2022-06-03 01:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20220603_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='code',
            field=models.CharField(default='M6?^0#.CeaYE!2,ZyC<4c(FX5G_QMOBm3*7hr_vVEY,88p5v1,MKGxJZlD&$5cxUT%I7A0UlcSgC2AjlPVjXlX!0IZw(Y.i7M-*+r&AFw!*dH4pOcuX', max_length=128),
        ),
        migrations.AlterField(
            model_name='otpmodel',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 3, 1, 56, 4, 137637, tzinfo=utc)),
        ),
    ]