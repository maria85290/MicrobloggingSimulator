# Generated by Django 3.2.8 on 2021-12-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20211211_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='UserId',
            field=models.IntegerField(default=0),
        ),
    ]
