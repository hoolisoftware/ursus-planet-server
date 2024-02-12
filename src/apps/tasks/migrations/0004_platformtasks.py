# Generated by Django 4.2.9 on 2024-02-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_social_reward', models.PositiveIntegerField()),
                ('task_social_is_active', models.BooleanField()),
                ('task_email_reward', models.PositiveIntegerField()),
                ('task_email_is_active', models.BooleanField()),
                ('task_username_reward', models.PositiveIntegerField()),
                ('task_username_is_active', models.BooleanField()),
                ('task_domain_id_reward', models.PositiveIntegerField()),
                ('task_domain_id_is_active', models.BooleanField()),
                ('task_avatar_reward', models.PositiveIntegerField()),
                ('task_avatar_is_active', models.BooleanField()),
                ('task_nft_avatar_reward', models.PositiveIntegerField()),
                ('task_nft_avatar_is_active', models.BooleanField()),
                ('task_ursas_collection_nft_avatar_reward', models.PositiveIntegerField()),
                ('task_ursas_collection_nft_avatar_is_active', models.BooleanField()),
                ('task_wallet_reward', models.PositiveIntegerField()),
                ('task_wallet_is_active', models.BooleanField()),
                ('task_chain_reward', models.PositiveIntegerField()),
                ('task_chain_is_active', models.BooleanField()),
                ('task_referral_reward', models.PositiveIntegerField()),
                ('task_referral_is_active', models.BooleanField()),
                ('task_email_notification_reward', models.PositiveIntegerField()),
                ('task_email_notification_is_active', models.BooleanField()),
                ('task_cabinet_notification_reward', models.PositiveIntegerField()),
                ('task_cabinet_notification_is_active', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
