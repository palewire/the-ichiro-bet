# Generated by Django 2.0.3 on 2018-03-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ichiro', '0002_auto_20180331_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projection',
            name='projection',
            field=models.CharField(choices=[('steamer-update', 'STEAMER (Update)'), ('the-bat-ros', 'The Bat (RoS)')], max_length=500),
        ),
    ]
