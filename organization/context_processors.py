from .models import Organization, organizationOverview
import logging
logger = logging.getLogger('django')

def menu_links(request):
    links = organizationOverview.objects.select_related('organization').get(organization=1, organization__is_church='True')


    return dict(org_links=links)
