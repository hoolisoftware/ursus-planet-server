# Generated by Django 4.2.9 on 2024-02-10 16:43

import apps.tasks.socials.discord.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('discord', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelMessageImageTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reward', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='tasks/discord/channel_message_image_task')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=(apps.tasks.socials.discord.models.ChannelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ChannelMessageTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reward', models.PositiveIntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=(apps.tasks.socials.discord.models.ChannelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PostReactionTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reward', models.PositiveIntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=(apps.tasks.socials.discord.models.PostMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ServerBoostTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reward', models.PositiveIntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=(apps.tasks.socials.discord.models.ServerMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ServerRoleTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reward', models.PositiveIntegerField()),
                ('role', models.CharField(max_length=64)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=(apps.tasks.socials.discord.models.ServerMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ServerSubscribeTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reward', models.PositiveIntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'abstract': False,
            },
            bases=(apps.tasks.socials.discord.models.ServerMixin, models.Model),
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]