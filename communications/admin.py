from django.contrib import admin
from .models import Enquiry

# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'subject', 'channel', 'created_date')
    list_filter = ['channel', 'created_date']
    list_per_page = 20

admin.site.register(Enquiry, EnquiryAdmin)
