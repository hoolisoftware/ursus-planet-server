from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


User = get_user_model()


class Season(models.Model):
    CHOICES_TYPE_PRIZE = (
        ('coin', 'Coin'),
        ('nft', 'NFT'),
        ('wl', 'WL')
    )
    CHOICES_TYPE_DISTRIBUTION = (
        ('raffle', 'Raffle'),
        ('airdrop', 'Airdrop')
    )

    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    time_base_of_game = models.PositiveIntegerField(verbose_name='Base time of game (hours)')  # noqa
    time_increase = models.PositiveIntegerField(verbose_name='Increase time (hours)')  # noqa
    win_count = models.PositiveIntegerField(verbose_name='Win first')

    type_prize = models.CharField(max_length=32, choices=CHOICES_TYPE_PRIZE)
    type_distribution = models.CharField(max_length=32, choices=CHOICES_TYPE_DISTRIBUTION)  # noqa
    base_coin = models.CharField(max_length=8)
    start_price = models.FloatField()

    @property
    def title(self):
        return f'Season #{self.id}'

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.type_distribution == 'raffle' and self.win_count != 1:
            raise ValidationError('Win can be only 1 if type of distribution is "raffle"')  # noqa

        if self.datetime_start > self.datetime_end:
            raise ValidationError('Season end date must be greater than start date')  # noqa

        if self.datetime_start < Season.objects.latest('id').datetime_end:
            raise ValidationError(f'Season can start only after end of previous season {Season.objects.latest("id").datetime_end}')  # noqa

    def __str__(self):
        return self.title


class SeasonParticipation(models.Model):
    season = models.ForeignKey(to=Season, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('season', 'user')

    def __str__(self):
        return f'{self.season.title} <= {self.user}'


class BasePrize(models.Model):
    image = models.ImageField(upload_to='seasons/prize/image/')
    season = models.OneToOneField(Season, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class PrizeCoin(BasePrize):
    coin_ticker = models.CharField(max_length=64)
    coin_count = models.FloatField()


class PrizeNft(BasePrize):
    collection_name = models.CharField(max_length=128)
    collection_link = models.URLField()
    nft_number = models.PositiveIntegerField()


class PrizeWl(BasePrize):
    whitelist_name = models.CharField(max_length=128)
    whitelist_count = models.PositiveIntegerField()
