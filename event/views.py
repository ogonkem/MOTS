from django.shortcuts import render
from django.views.generic import View
from .models import ActualEvent, Event, EventPhoto, EventAudio, EventVideo, EventVideo, Preacher
import logging
logger = logging.getLogger('django')

# Create your views here.
class EventView(View):
    template_name = "event/event.html"

    def get(self, request, event_id):
        events = Event.objects.select_related('event').filter(id = event_id).values(
            'event_id',
            'event__name',
            'event__description',
            'date',
            'end_date',
            'address_line_1',
            'address_line_2',
            'city',
            'state',
            'country',
            'type'

        ).first()
        
        photos = EventPhoto.objects.filter(event = events['event_id']).values('name','file')
        photo = photos.first()
        videos = EventVideo.objects.filter(event = events['event_id']).values('name', 'youtube_link')
        preachers = Preacher.objects.select_related('staff').filter(event = events['event_id']).values(
            'first_name', 'last_name', 'staff__photo', 'staff__job_title', 'email', 'is_host')

        logger.info(photo)

        context = {
            'events': events,
            'photos': photos,
            'photo': photo,
            'videos': videos,
            'preachers': preachers,
        }

        return render(request, self.template_name, context)
