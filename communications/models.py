from django.db import models

# Create your models here.
channel_chioce = (
    (0,'Select How you heard about us'),
    ('Facebook','Facebook'),
    ('Instagram', 'Instagram'),
    ('Google','Google'),
    ('word of mouth','Word of Mouth'),
    ('youtube','Youtube'),
    ('Ads','Ads'),
    ('others','Others'),
)


class Enquiry(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    channel = models.CharField(max_length=100, choices=channel_chioce, default=0)

    class Meta:
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f"{self.email}_{self.created_date}"

