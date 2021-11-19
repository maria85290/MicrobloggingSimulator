# Generated by Django 3.2.8 on 2021-11-18 11:22

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
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personality', models.IntegerField(blank=True)),
                ('durationParticipation', models.TimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('image', models.CharField(blank=True, max_length=50)),
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
                ('replyContent', models.CharField(blank=True, max_length=280)),
                ('actionType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.action_type')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.participant')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.post')),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashtag', models.CharField(blank=True, max_length=30)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tweets.post')),
            ],
        ),
    ]