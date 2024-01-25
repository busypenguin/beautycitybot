# Generated by Django 5.0.1 on 2024-01-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saloons', '0003_alter_saloon_options_alter_saloon_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('saloons', models.ManyToManyField(blank=True, related_name='saloon_masters', to='saloons.service')),
                ('services', models.ManyToManyField(blank=True, related_name='masters', to='saloons.service')),
            ],
        ),
    ]
