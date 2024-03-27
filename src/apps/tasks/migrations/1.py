# Generated by Django 4.2.9 on 2024-03-26 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referral_interest', models.PositiveIntegerField(default=0, verbose_name='Referral interest (%)')),
                ('cancel_fee', models.PositiveIntegerField(default=0, verbose_name='Task cancel fee (%)')),
            ],
            options={
                'verbose_name_plural': 'Tasks settings',
            },
        ),
    ]