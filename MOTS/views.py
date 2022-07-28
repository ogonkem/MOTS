from django.shortcuts import render
from django.views.generic import View
from organization.models import Organization
from staff.models import Staff
from blog.models import Article, Author, Paragraph
from testimony.models import Testimony
from event.models import ActualEvent, WeeklyEvent, EventPhoto
import logging
logger = logging.getLogger('django')

class HomeView(View):
    def get(self, request, *args, **kwargs):
        events_photos = EventPhoto.objects.select_related('event').all().values(
            'name',
            'file',
            'created_date',
            'event__name'


        )

        weekly_events = WeeklyEvent.objects.select_related('event').filter(organization=1, organization__is_church='True').values(
            'day',
            'time',
            'end_time',
            'city',
            'state',
            'event__name'


        )

        staff = Staff.objects.prefetch_related('organization').get(organization=1, organization__is_church='True', job_title = 'General Overseer')
        testimonies = Testimony.objects.filter(verified=True)[:3].values(
            'first_name',
            'last_name',
            'title',
            'description'
        )

        articles = Article.objects.all()[:3]
        dispaly_paragraph = []
        for article in articles:
            paragraph =  Paragraph.objects.filter(article=article).first()
            paragraph_dict = dict(
                id = paragraph.article.id,
                content = ' '.join(word for word in paragraph.paragraph_content.split(' ')[:28] if word != '/n/n') + '...'

            )
            # logger.info(paragraph.paragraph_content.split(' ')[:24])
            dispaly_paragraph.append(paragraph_dict)

        context = {
            'events_photos': events_photos,
            'weekly_events': weekly_events,
            'testimonies': testimonies,
            'staff': staff,
            'articles': articles,
            'dispaly_paragraph': dispaly_paragraph,
        }

        return render(request, 'church/home.html', context)

class AboutView(View):
    def get(self, request, *args, **kwargs):
        weekly_events = WeeklyEvent.objects.prefetch_related('organization').filter(organization=1, organization__is_church='True').values()
        staff = Staff.objects.prefetch_related('organization').get(organization=1, organization__is_church='True')
        testimonies = Testimony.objects.filter(verified=True)[:3].values(
            'first_name',
            'last_name',
            'title',
            'description'
        )

        context = {
            'weekly_events': weekly_events,
            'testimonies': testimonies,
            'staff': staff,
        }

        return render(request, 'church/about.html', context)
