from django.db import models
from django.urls import reverse

# Create your models here.
class Testimony(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2500)
    created_date = models.DateTimeField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/testimony', blank=True, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'testimony'
        verbose_name_plural = 'testimonies'

    def __str__(self):
        return self.title
