from django.db import models
from organization.models import Organization
from datetime import datetime
from staff.models import Staff
from django.urls import reverse

# Create your models here.
day_choice = (
    (0,'Select Day of Week'),
    ('Monday','Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
)
type_choice = (
    (0,'Select Event Type'),
    ('Crusade','Crusade'),
    ('Outreach', 'Outreach'),
    ('Concert','Concert'),
)

class ActualEvent(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class WeeklyEvent(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    day = models.CharField(max_length=50, choices=day_choice, default=0)
    time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(ActualEvent, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Weekly Event'
        verbose_name_plural = 'Weekly Events'

    def __str__(self):
        return f"{self.event} on {self.day} by {self.time}"

class Event(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False)
    end_date = models.DateTimeField(auto_now=False)
    address_line_1 = models.CharField(max_length=50, blank=True)
    address_line_2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=50, choices=type_choice, default=0)
    event = models.ForeignKey(ActualEvent, on_delete=models.CASCADE, blank=True, null=True)

    def get_url(self):
        return reverse('event', args=[self.id])

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f"{self.event} on {self.date}"

class EventPhoto(models.Model):
    event = models.ForeignKey(ActualEvent, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    file = models.ImageField(upload_to='photos/event')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class EventVideo(models.Model):
    event = models.ForeignKey(ActualEvent, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    youtube_link = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class EventAudio(models.Model):
    event = models.ForeignKey(ActualEvent, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    file = models.ImageField(upload_to='photos/Audio')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Preacher(models.Model):
    event = models.ManyToManyField(ActualEvent)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=50)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_host = models.BooleanField(default=False)
    title = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='photos/preacher', blank=True, null=True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
