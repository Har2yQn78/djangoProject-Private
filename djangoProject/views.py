from django.http import HttpResponse
import random
from django.template.loader import render_to_string, get_template
from articles.models import Article


def home_view(request, *args, **kwargs):
    number = random.randint(1, 5)
    article_obj = Article.objects.get(id=number)
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    name = "Harry"
    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)
