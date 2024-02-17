# Generated by Django 4.2.9 on 2024-02-11 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_initial'),
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channelboosttask',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_channel_boost', to='tasks.projectproxy'),
        ),
        migrations.AlterField(
            model_name='channeljointask',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_channel_join', to='tasks.projectproxy'),
        ),
        migrations.AlterField(
            model_name='channelreactiontask',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_channel_reaction', to='tasks.projectproxy'),
        ),
        migrations.AlterField(
            model_name='groupjointask',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_group_join', to='tasks.projectproxy'),
        ),
        migrations.AlterField(
            model_name='groupmessagetask',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_group_message', to='tasks.projectproxy'),
        ),
    ]