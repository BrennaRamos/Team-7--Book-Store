# Generated by Django 2.2.5 on 2019-10-11 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_review_anonymity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='anonymity',
            field=models.CharField(choices=[('Username', 'Username'), ('Anonymous', 'Anonymous')], default='Username', max_length=50),
        ),
    ]