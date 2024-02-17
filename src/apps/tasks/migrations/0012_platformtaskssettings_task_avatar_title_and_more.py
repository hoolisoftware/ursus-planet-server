# Generated by Django 4.2.9 on 2024-02-17 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_platformtaskssettings_task_chain_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_avatar_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_cabinet_notification_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_chain_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_domain_id_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_email_notification_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_email_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_nft_avatar_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_referral_self_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_referral_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_social_discord_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_social_github_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_social_telegram_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_social_x_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_ursas_collection_nft_avatar_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_username_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_wallet_title',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]