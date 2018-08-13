from django.db import models


class Stock(models.Model):
    # 'username' for the stock market
    ticker = models.CharField(max_length=10)
    # price at the beginning of the day
    open = models.FloatField()
    # price at the end of the day
    close = models.FloatField()
    # how many times people traded it during the day
    volume = models.IntegerField()

    def __str__(self):
        return self.ticker