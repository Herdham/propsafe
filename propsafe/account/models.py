from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.conf import settings

class UserAccount(AbstractUser):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)

class Profile(models.Model):
    class ExperienceLevel(models.TextChoices):
        beginner = ('BG', 'Beginner')
        intermediate = ('INT', 'Intermediate')
        advanced = ('ADV', 'Advanced')
        professional = ('PROF', 'Professional')

    class PreferredMarket(models.TextChoices):
        forex = ('fx', 'Forex')
        cypto = ('cyp', 'Cypto')
        stocks = ('stc', 'Stocks')
        indices = ('ind', 'Indices')
        commodities = ('comm', 'Commodities')

    class ConnectionType(models.TextChoices):
        manual = ('mn', 'manual')
        mt5 = ('mt5', 'MT5')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to="profile/", blank=True, null=True)
    bio = models.TextField(blank=True, null=True, default='')
    country = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.BigIntegerField(blank=True, null=True)
    experience_level = models.CharField(max_length=150, blank=True, null=True)
    timezone = models.CharField(max_length=150, blank=True, null=True)
    preferred_market = models.CharField(max_length=150, blank=True, null=True)
    favourite_pair = models.CharField(max_length=150, blank=True, null=True, default='')
    account_size = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    risk_per_trade = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    daily_loss_limit = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    daily_profit_target = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    connection_type = models.CharField(max_length=150, choices=ConnectionType.choices, default=ConnectionType.manual)
    joined_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}_profile{self.id}"