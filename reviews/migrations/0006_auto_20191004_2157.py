# Generated by Django 2.2.5 on 2019-10-05 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20191004_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)]),
        ),
    ]
