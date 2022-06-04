# Generated by Django 3.2.13 on 2022-06-04 17:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_auto_20220604_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='code',
            field=models.CharField(default='%.?sUpBwgXBFo=suEqabm#G?t9(%bB^K#9aDKBz&u+^Er+_I4AomT?PQaI#,1I.RHIV3pgs>P_!MvZeK&,^M(z>pjx!l8I03=', max_length=128),
        ),
        migrations.AlterField(
            model_name='otpmodel',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 17, 50, 13, 6770, tzinfo=utc)),
        ),
    ]
