# Generated by Django 4.2.9 on 2024-02-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_alter_user_points_alter_user_points_referral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='points',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='points_referral',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
