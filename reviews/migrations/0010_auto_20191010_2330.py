# Generated by Django 2.2.5 on 2019-10-11 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20191010_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='anonymity',
            field=models.BooleanField(default=False),
        ),
    ]
