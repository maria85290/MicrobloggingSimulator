# Generated by Django 3.2.8 on 2022-04-06 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configName', models.CharField(max_length=10)),
                ('space_for_comment', models.BooleanField(default=0)),
                ('space_for_creat_post', models.BooleanField(default=0)),
                ('user_picture', models.BooleanField(default=0)),
                ('reply_button', models.BooleanField(default=0)),
                ('like_button', models.BooleanField(default=0)),
                ('share_button', models.BooleanField(default=0)),
                ('block_button', models.BooleanField(default=0)),
                ('follow_button', models.BooleanField(default=0)),
                ('retweet_button', models.BooleanField(default=0)),
                ('posts_number', models.IntegerField(default=1)),
                ('lower_limit_interaction', models.IntegerField(default=1)),
                ('upper_limit_interaction', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personality', models.IntegerField(default=0)),
                ('date', models.DateField(default='2020/01/01')),
                ('beginTime', models.TimeField()),
                ('endTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
            ],
        ),
        migrations.CreateModel(
            name='Post_by_participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.participant')),
            ],
        ),
        migrations.CreateModel(
            name='Mouse_tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking', models.CharField(max_length=100)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.participant')),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.action_type')),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.configuration')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.participant')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.post')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagepath', models.CharField(max_length=50)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tweets.post')),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(max_length=20)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tweets.post')),
            ],
        ),
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.configuration')),
            ],
        ),
        migrations.CreateModel(
            name='action_reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('interaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.interaction')),
            ],
        ),
    ]
