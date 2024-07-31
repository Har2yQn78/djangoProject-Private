from django.test import TestCase
from django.utils.text import slugify
from .models import Article
from .utils import slugify_instance_title
# Create your tests here.


class ArticleTestCase(TestCase):
    def setUp(self):
        self.number_of_Article = 500
        for i in range(0, self.number_of_Article):
            Article.objects.create(title='test slug', content='testing again')

    def test_queryset_exists(self):
        qs = Article.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = Article.objects.all()
        self.assertEqual(qs.count(), self.number_of_Article)

    def test_hello_world_slug(self):
        obj = Article.objects.all().order_by("id").first()
        title = obj.title
        slug = obj.slug
        slugify_title = slugify(title)
        self.assertEqual(slug, slugify_title)

    def test_hello_world_unique_slug(self):
        qs = Article.objects.exclude(slug__iexact='test-slug')
        for obj in qs:
            title = obj.title
            slug = obj.slug
            slugify_title = slugify(title)
            self.assertNotEqual(slug, slugify_title)

    def test_slugify_instance_title(self):
        obj = Article.objects.all().last()
        new_slug = []
        for i in range(0, 25):
            instance = slugify_instance_title(obj, save=False)
            new_slug.append(instance.slug)
        unique_slug = list(set(new_slug))
        self.assertEqual(len(new_slug), len(unique_slug))

    def test_slugify_instance_title_redux(self):
        slug_list = Article.objects.all().values_list('slug', flat=True)
        unique_slug_list = list(set(slug_list))
        self.assertEqual(len(slug_list), len(unique_slug_list))

    def test_article_search_manager(self):
        qs = Article.objects.search(query='test slug')
        self.assertEqual(qs.count(), self.number_of_Article)
        qs = Article.objects.search(query='slug')
        self.assertEqual(qs.count(), self.number_of_Article)
        qs = Article.objects.search(query='testing again')
        self.assertEqual(qs.count(), self.number_of_Article)

