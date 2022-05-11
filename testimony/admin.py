from django.contrib import admin
from .models import Testimony

# Register your models here.
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'title', 'verified', 'created_date')
    list_editable = ('verified',)
    list_filter = ('verified', 'created_date')

admin.site.register(Testimony, TestimonyAdmin)
