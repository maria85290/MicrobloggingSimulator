# Generated by Django 3.2.8 on 2021-12-12 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0008_alter_participant_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_by_participant',
            name='configuration',
        ),
    ]
