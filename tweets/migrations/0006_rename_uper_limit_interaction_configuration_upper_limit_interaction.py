# Generated by Django 3.2.8 on 2021-11-24 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20211124_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuration',
            old_name='uper_limit_interaction',
            new_name='upper_limit_interaction',
        ),
    ]
