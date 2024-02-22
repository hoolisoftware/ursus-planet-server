# Generated by Django 4.2.9 on 2024-02-22 10:46

import apps.users.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_user_points_alter_user_points_referral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='referral_quote',
            field=models.PositiveIntegerField(default=apps.users.utils.default_referral_quote),
        ),
    ]