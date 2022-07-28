from django.shortcuts import render
from django.views.generic import View
from .models import Event, EventPhoto, EventVideo, EventVideo, Preacher
from django.db.models import Q
import logging
logger = logging.getLogger('django')

# Create your views here.
class EventView(View):
    template_name = "event/event.html"

    def get(self, request, event_id):
        events = Event.objects.all()
        events_list = []
        for e in events:
            event_dict = dict(
                id=e.id,
                name = e.event.name,
                date = e.date,
                city = e.city,
                state = e.state,
                url = e.get_url
            )
            events_list.append(event_dict)

        event = Event.objects.select_related('event').filter(id = event_id).values(
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
        
        photos = EventPhoto.objects.filter(event = event['event_id']).values('name','file')
        photo = photos.first()
        videos = EventVideo.objects.filter(event = event['event_id']).values('name', 'youtube_link')
        preachers = Preacher.objects.select_related('staff').filter(event = event['event_id']).values(
            'first_name', 'last_name', 'staff__photo', 'staff__job_title', 'email', 'is_host')

        context = {
            'events_list': events_list,
            'event': event,
            'photos': photos,
            'photo': photo,
            'videos': videos,
            'preachers': preachers,
        }

        return render(request, self.template_name, context)

class SearchView(View):
    template_name = "event/event_search.html"

    def post(self, request):
        if 'keyword' in request.POST:
            keyword = request.POST['keyword']
            qs = Q(event__name__icontains=keyword) | Q(event__name__icontains=keyword) | Q(city__icontains=keyword) | Q(country__icontains=keyword)
            events = Event.objects.select_related('event').filter(qs).order_by('-id')           
        else:
            events = Event.objects.select_related('event').all().order_by('-id')
        
        events_list = []
        for event in events:
            event_dict = dict(
                id=event.id,
                name = event.event.name,
                desc = event.event.description[:300] + '...',
                date = event.date,
                end_date = event.end_date,
                created_date = event.created_date,
                preacher = Preacher.objects.filter(event = event.event).values('first_name', 'last_name',).first(),
                photo = EventPhoto.objects.filter(event = event.event).values('file').first(),
                event_url = event.get_url
            )
            events_list.append(event_dict)

        logger.info(events_list)


        context = {
            'events_list': events_list,
        }

        return render(request, self.template_name, context)