# Generated by Django 4.2.9 on 2024-02-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0010_platformtaskssettings_task_avatar_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformtaskssettings',
            name='task_chain_link',
            field=models.BooleanField(default=False),
        ),
    ]
