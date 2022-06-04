# Generated by Django 3.2.13 on 2022-06-04 17:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_auto_20220604_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='code',
            field=models.CharField(default='a$zw1V9+Z(Kh+34&MbgHkJQ6JtF(URtrPxs*Q5xHl0eW7gB,YEMiBh&.igHKsc6_Pa&S0iI_QOv6v?am_cJ+v?+t2d', max_length=128),
        ),
        migrations.AlterField(
            model_name='otpmodel',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 17, 50, 49, 70177, tzinfo=utc)),
        ),
    ]
