from django.contrib import admin
from .models import ActualEvent, WeeklyEvent, Event, EventPhoto, EventVideo, EventAudio, Preacher

# Register your models here.
class ActualEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date' )
    list_filter = ['created_date']
    list_per_page = 20


class WeeklyEventAdmin(admin.ModelAdmin):
    list_display = ('organization', 'event', 'day', 'time', 'end_time', 'created_date' )
    list_editable = ['event']
    list_filter = ['created_date']
    list_per_page = 20

class EventAdmin(admin.ModelAdmin):
    list_display = ('organization', 'event', 'date', 'end_date', 'created_date' )
    list_editable = ['event']
    list_filter = ['created_date']
    list_per_page = 20

class EventPhotoAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'created_date' )
    list_filter = ['created_date']
    list_per_page = 20

class EventVideoAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'created_date' )
    list_filter = ['created_date']
    list_per_page = 20

class EventAudioAdmin(admin.ModelAdmin):
    list_display = ('event', 'name', 'created_date' )
    list_filter = ['created_date']
    list_per_page = 20

class PreacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_host', 'created_date' )
    list_filter = ['created_date']
    list_editable = ['is_host']
    list_per_page = 20



admin.site.register(ActualEvent, ActualEventAdmin)
admin.site.register(WeeklyEvent, WeeklyEventAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventPhoto, EventPhotoAdmin)
admin.site.register(EventVideo, EventVideoAdmin)
admin.site.register(EventAudio, EventAudioAdmin)
admin.site.register(Preacher, PreacherAdmin)
