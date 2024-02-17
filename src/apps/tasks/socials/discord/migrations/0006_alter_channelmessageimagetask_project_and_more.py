# Generated by Django 4.2.9 on 2024-02-11 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_initial'),
        ('discord', '0005_alter_channelmessageimagetask_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelmessageimagetask',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discord_channel_message_image', to='tasks.projectproxy'),
        ),
        migrations.AlterField(
            model_name='channelmessagetask',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discord_channel_message', to='tasks.projectproxy'),
        ),
        migrations.AlterField(
            model_name='postreactiontask',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discord_channel_reaction', to='tasks.projectproxy'),
        ),
        migrations.AlterField(
            model_name='serverboosttask',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discord_server_boost', to='tasks.projectproxy'),
        ),
        migrations.AlterField(
            model_name='serverroletask',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discord_server_role', to='tasks.projectproxy'),
        ),
        migrations.AlterField(
            model_name='serversubscribetask',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discord_server_subscribe', to='tasks.projectproxy'),
        ),
    ]