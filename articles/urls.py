from django.urls import path

from .views import (
    article_search_view,
    article_create_view,
    article_detail_view,
    article_image_upload_view,
)

app_name = 'articles'
urlpatterns = [
    path('', article_search_view, name='search'),
    path('create/', article_create_view, name='create'),
    path("create/image-upload/", article_image_upload_view),
    path('<slug:slug>/', article_detail_view, name='detail'),
]
