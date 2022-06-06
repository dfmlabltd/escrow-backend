# Generated by Django 3.2.13 on 2022-06-06 00:12

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0049_auto_20220605_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpmodel',
            name='code',
            field=models.CharField(default=user.models.compute_otp, max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='otpmodel',
            name='expiry_time',
            field=models.DateTimeField(default=user.models.compute_expiry_time),
        ),
    ]
