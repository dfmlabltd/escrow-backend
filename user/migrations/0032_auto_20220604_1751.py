# Generated by Django 3.2.13 on 2022-06-04 17:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0031_auto_20220604_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='code',
            field=models.CharField(default='F!n6I3jIoo)Jvzk9VinP%blGnnBE#mkHpGBLn-*4KrkpYb2s4rhi-kut&>uIJ&C*<wYs>,FT8c<vgZP&XJ%)Gihopj%rzOR%=2!XB.LEu_uMm9h47IG', max_length=128),
        ),
        migrations.AlterField(
            model_name='otpmodel',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 17, 56, 40, 523121, tzinfo=utc)),
        ),
    ]