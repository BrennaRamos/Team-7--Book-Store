# Generated by Django 2.2.5 on 2019-10-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_auto_20190929_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='photo',
            field=models.ImageField(default=1, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
