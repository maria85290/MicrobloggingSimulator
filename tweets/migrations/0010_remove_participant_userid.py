# Generated by Django 3.2.8 on 2021-12-13 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0009_remove_post_by_participant_configuration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='UserId',
        ),
    ]