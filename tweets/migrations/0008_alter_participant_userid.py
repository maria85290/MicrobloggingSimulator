# Generated by Django 3.2.8 on 2021-12-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0007_alter_participant_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='UserId',
            field=models.IntegerField(default=0),
        ),
    ]