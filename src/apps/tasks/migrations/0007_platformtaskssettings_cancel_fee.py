# Generated by Django 4.2.9 on 2024-02-17 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_platformtaskssettings_task_username_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformtaskssettings',
            name='cancel_fee',
            field=models.PositiveIntegerField(default=0, verbose_name='Task cancel fee (%)'),
        ),
    ]
