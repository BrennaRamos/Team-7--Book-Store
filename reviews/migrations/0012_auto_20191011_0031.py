# Generated by Django 2.2.5 on 2019-10-11 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20191010_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.CharField(max_length=800),
        ),
    ]
