from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class Case(models.Model):
    STATUS = [
        ('a', 'Active'),
        ('s', 'Soon'),
        ('e', 'Ended'),
    ]
    title = models.CharField(max_length=300, verbose_name=_('title'))
    maker = models.CharField(max_length=100, verbose_name=_('maker'))
    city = models.CharField(max_length=100, verbose_name=_('city'))
    region = models.CharField(max_length=100, verbose_name=_('region'))
    capacity = models.PositiveIntegerField(blank=True, verbose_name=_('capacity'))
    meter = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(100)], verbose_name=_('meter'))
    base_value = models.PositiveIntegerField(verbose_name=_('base value'))
    buy_assurance = models.BooleanField(default=False, verbose_name=_('buy insurance'))
    guaranteed_gain = models.BooleanField(default=False, verbose_name=_('guaranteed gain'))
    guaranteed_gain_percent = models.PositiveIntegerField(verbose_name=_('guaranteed gain percent'))
    end_time = models.CharField(max_length=200, verbose_name=_('end time'))
    description = models.TextField(max_length=500, verbose_name=_('description'))
    status = models.CharField(max_length=10, choices=STATUS, verbose_name=_('status'))
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True, allow_unicode=True)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Case, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-datetime_created',)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('product_detail', args=[self.slug])


