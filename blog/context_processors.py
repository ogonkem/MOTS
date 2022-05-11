from blog.models import Article, Author, Paragraph
import logging
logger = logging.getLogger('django')

def menu_links(request):
    links = Article.objects.filter().order_by('-id')[:3].values('article_title', 'created_date')


    return dict(blog_links=links)
