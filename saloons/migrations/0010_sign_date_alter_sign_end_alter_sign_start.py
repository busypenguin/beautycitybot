# Generated by Django 4.2.9 on 2024-01-25 22:27

import datetime
from django.db import migrations, models
import saloons.validators


class Migration(migrations.Migration):

    dependencies = [
        ('saloons', '0009_service_duration_service_price_alter_service_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sign',
            name='date',
            field=models.DateField(default=datetime.date(2024, 1, 26)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sign',
            name='end',
            field=models.TimeField(validators=[saloons.validators.validate_work_hours]),
        ),
        migrations.AlterField(
            model_name='sign',
            name='start',
            field=models.TimeField(validators=[saloons.validators.validate_work_hours]),
        ),
    ]
