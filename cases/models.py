from django.db import models

class Case(models.Model):
    STATUS = [
        ('a', 'Active'),
        ('s', 'Soon'),
        ('e', 'Ended'),
    ]

    title = models.CharField(max_length=300)
    maker = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    meter = models.PositiveIntegerField()
    base_value = models.PositiveIntegerField()
    buy_assurance = models.BooleanField(default=False)
    guaranteed_gain = models.BooleanField(default=False)
    guaranteed_gain_percent = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True, allow_unicode=True)
    datetime_created = models.DateTimeField(auto_now_add=True)


