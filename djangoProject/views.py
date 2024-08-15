"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request, *args, **kwargs):

    name = "Harry"  # hard coded
    random_id = random.randint(1, 4)  # pseudo random

    # from the database??
    article_obj = Article.objects.all().first()
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
    }
    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)