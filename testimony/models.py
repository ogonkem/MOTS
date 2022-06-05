from django.db import models

# Create your models here.
class Testimony(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=2500)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    verified = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/testimony', blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Testimony'
        verbose_name_plural = 'Testimonies'

    def __str__(self):
        return f"{self.email}_{self.created_date}"
