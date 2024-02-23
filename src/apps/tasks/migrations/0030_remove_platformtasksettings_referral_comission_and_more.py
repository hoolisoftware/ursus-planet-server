# Generated by Django 4.2.9 on 2024-02-23 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0029_rename_task_cabinet_notification_account_is_active_platformtasksettings_task_cabinet_notifications_a'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='referral_comission',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_avatar_nft_is_active',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_avatar_nft_link',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_avatar_nft_reward',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_avatar_nft_title',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_avatar_nft_ursas_is_active',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_avatar_nft_ursas_link',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_avatar_nft_ursas_reward',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_avatar_nft_ursas_title',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_chain_is_active',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_chain_link',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_chain_reward',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_chain_title',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_username_domain_id_is_active',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_username_domain_id_link',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_username_domain_id_reward',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_username_domain_id_title',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_wallet_is_active',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_wallet_link',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_wallet_reward',
        ),
        migrations.RemoveField(
            model_name='platformtasksettings',
            name='task_wallet_title',
        ),
        migrations.AddField(
            model_name='platformtasksettings',
            name='referral_interest',
            field=models.PositiveIntegerField(default=0, verbose_name='Referral interest (%)'),
        ),
        migrations.AlterField(
            model_name='platformtasklog',
            name='task',
            field=models.CharField(choices=[('task_username', 'Task - set username'), ('task_email', 'Task - set email'), ('task_avatar', 'Task - set avatar'), ('task_referrer', 'Task = set referrer'), ('task_cabinet_notifications_account', 'Task - enable cabinet account notifications'), ('task_cabinet_notifications_email', 'Task - enable cabinet email notifications'), ('task_social_discord', 'Task - connect Discord account'), ('task_social_github', 'Task - connect Github account'), ('task_social_telegram', 'Task - connect Telegram account'), ('task_social_x', 'Task - connect X account')], max_length=128),
        ),
    ]
