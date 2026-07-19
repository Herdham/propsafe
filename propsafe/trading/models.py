from django.db import models
from django.conf import settings

# Create your models here.
class Trade(models.Model):
    class Status(models.TextChoices):
        open = ('op', 'Open')
        closed = ('cl', 'Closed')
        breakeven = ('be', 'Breakeven')

    class Result(models.TextChoices):
        win = ('w', 'win')
        loss = ('cl', 'loss')
        breakeven = ('be', 'BE')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="trade")
    instrument = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)
    entry_price = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    exit_price = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    position_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    stop_loss = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    take_profit = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    risk_per_trade = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    leverage = models.CharField(max_length=100)
    account_balance = models.DecimalField(max_digits=15, decimal_places=2)
    risk_percent = models.CharField(max_length=100)
    risk_amount = models.CharField(max_length=100)
    profit_and_loss = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    profit_percent = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    potential_reward = models.DecimalField(max_digits=15, decimal_places=2)
    expected_outcome = models.CharField(max_length=100)
    actual_outcome = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    setup = models.CharField(max_length=100)
    timeframe = models.CharField(max_length=5)
    session = models.CharField(max_length=100)
    entry_date = models.CharField(max_length=100)
    trade_notes = models.TextField(blank=True, null=True, default='')
    emotion_before = models.CharField(max_length=100)
    emotion_during = models.CharField(max_length=100)
    emotion_after = models.CharField(max_length=100)
    lesson_learned = models.TextField(blank=True, null=True, default='')
    news_checked = models.BooleanField(default=False)
    followed_confirmation = models.BooleanField(default=False)
    followed_plan = models.BooleanField(default=False)
    risk_under_one_percent = models.BooleanField(default=False)
    avoided_revenge_trade = models.BooleanField(default=False)
    avoided_fomo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class TradeScreenShot(models.Model):
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE, related_name="trade_screenshot")
    image = models.ImageField(upload_to="screenshot", blank=True, null=True, default='')
    caption = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"trade_screenshot by {self.trade.user.username}"


class StreakModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="streak")
    current_streak = models.IntegerField(default=0)
    best_streak = models.IntegerField(default=0)
    updated_at = models.DateField(auto_now=True)


class Badge(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="badges")
    badge_name = models.CharField(max_length=150, blank=True, null=True, default='')
    description = models.TextField()
    earned_at = models.DateTimeField(auto_now_add=True)