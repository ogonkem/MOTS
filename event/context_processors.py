from .models import Event
import logging
logger = logging.getLogger('django')

def event_links(request):
    links = Event.objects.select_related('event').all()
    return dict(event_links=links)
