from django.shortcuts import render
from django.views.generic import View
from blog.models import Article, Author, Paragraph
import logging
logger = logging.getLogger('django')
# Create your views here.

class ArticleView(View):
    def get(self, request, article_id):

        paragraphs = Paragraph.objects.select_related('articles').filter(article__id=article_id).values()
        articles = Article.objects.all().order_by('-id')[:3].values()
        authors = Author.objects.prefetch_related('article').filter(article__id=article_id).values()

        dispaly_paragraph = []
        for art in articles:
            paragraph =  Paragraph.objects.filter(article=art['id']).first()
            paragraph_dict = dict(
                id = paragraph.article.id,
                content = ' '.join(word for word in paragraph.paragraph_content.split(' ')[:28] if word != '/n/n') + '...',
                authors = Author.objects.filter(article__id=art['id']).first()
            )
            dispaly_paragraph.append(paragraph_dict)

        article = Article.objects.get(id=article_id)
        logger.info(articles)

        context = {
        'article': article,
        'articles': articles,
        'paragraphs': paragraphs,
        'authors': authors,
        'dispaly_paragraph': dispaly_paragraph,
        }

        return render(request, 'blog/article.html', context)

class BlogView(View):
    def get(self, request, keyword=None):
        if keyword != None:
            article_ids = []
            paragraphs = Paragraph.objects.select_related('articles').filter(paragraph_content__contains=keyword).values('id')
            for paragraph in paragraphs:
                if paragraph.id not in article_ids:
                        article_ids.append(article.id)

            articles = Article.objects.filter(id__in=article_ids).order_by('-id').values()
        else:
            articles = Article.objects.filter().order_by('-id').values()

        dispaly_paragraph = []
        for article in articles:
            paragraph =  Paragraph.objects.filter(article=article['id']).first()
            paragraph_dict = dict(
                id = paragraph.article.id,
                content = ' '.join(word for word in paragraph.paragraph_content.split(' ')[:28] if word != '/n/n') + '...',
                authors = Author.objects.filter(article__id=article['id']).first()
            )
            dispaly_paragraph.append(paragraph_dict)

        context = {
            'articles': articles,
            'dispaly_paragraph': dispaly_paragraph,
        }

        return render(request, 'blog/blog.html', context)

class ArticleSearchView(View):
    def get(self, request):
        if 'keyword' in request.GET:
            keyword = request.GET['keyword']
            if keyword:
                article_ids = []
                paragraphs = Paragraph.objects.select_related('articles').filter(paragraph_content__contains=keyword).values('id')
                for paragraph in paragraphs:
                    if paragraph['id'] not in article_ids:
                            article_ids.append(paragraph['id'])

                articles = Article.objects.filter(id__in=article_ids).order_by('-id').values()

        dispaly_paragraph = []
        for article in articles:
            paragraph =  Paragraph.objects.filter(article=article['id']).first()
            paragraph_dict = dict(
                id = paragraph.article.id,
                content = ' '.join(word for word in paragraph.paragraph_content.split(' ')[:28] if word != '/n/n') + '...',
                authors = Author.objects.filter(article__id=article['id']).first()
            )
            dispaly_paragraph.append(paragraph_dict)

        latest_articles = Article.objects.filter().order_by('-id')[:3]

        context = {
            'articles': articles,
            'dispaly_paragraph': dispaly_paragraph,
            'latest_articles': latest_articles,
        }

        return render(request, 'blog/blog.html', context)
