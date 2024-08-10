from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import ArticleForm, ArticleImageForm
from .models import Article


# Create your views here.

def article_search_view(request):
    query = request.GET.get('q')
    qs = Article.objects.search(query=query)
    context = {
        "object_list": qs
    }
    return render(request, "articles/search.html", context=context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm(request.POST or None)
        return redirect(article_object.get_absolute_url())
        # context['object'] = article_object
        # context['created'] = True
    return render(request, "articles/create.html", context=context)


def article_detail_view(request, slug=None):
    article_obj = None
    if id is not None:
        try:
            article_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj = Article.objects.filter(slug=slug).filter()
        except:
            raise Http404
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)


def article_image_upload_view(request, parent_id=None):
    try:
        parent_obj = Article.objects.get(id=parent_id, user=request.user)
    except:
        parent_obj = None
    if parent_obj is None:
        raise Http404
    form = ArticleImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.article = parent_obj 
        obj.save()
    return render(request, "image-form.html", {"form": form})
