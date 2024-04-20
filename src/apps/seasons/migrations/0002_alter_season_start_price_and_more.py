# Generated by Django 4.2.9 on 2024-04-20 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seasons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='start_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='season',
            name='type_distribution',
            field=models.CharField(choices=[('raffle', 'Raffle'), ('airdrop', 'Airdrop')], max_length=32),
        ),
        migrations.AlterField(
            model_name='season',
            name='type_prize',
            field=models.CharField(choices=[('coin', 'Coin'), ('nft', 'NFT'), ('wl', 'WL')], max_length=32),
        ),
    ]
