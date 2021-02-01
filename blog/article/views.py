from django.http import Http404
from django.views import generic
from django.db.models import Q
from article import models

from django.shortcuts import redirect


class ArticleList(generic.ListView):
    model = models.Article
    context_object_name = 'articles'
    paginate_by = 20
    allow_empty = True


class ArticleDetail(generic.DetailView):
    model = models.Article
    context_object_name = 'article'


class TagList(generic.ListView):
    model = models.Tag
    context_object_name = 'tags'


class TagDetail(generic.ListView):
    context_object_name = 'articles'
    paginate_by = 20
    template_name = 'article/tag_detail.html'
    allow_empty = True

    def get_queryset(self):
        try:
            tag = models.Tag.objects.get(pk=self.kwargs['pk'])
            self.extra_context = {'tag': tag}
        except models.Tag.DoesNotExist:
            raise Http404
        self.queryset = tag.articles.all()
        return super().get_queryset()


class ArchiveIndex(generic.ArchiveIndexView):
    model = models.Article
    context_object_name = 'articles'
    # paginate_by = 20
    date_field = 'posted_at'
    allow_empty = True


class YearArchive(generic.YearArchiveView):
    model = models.Article
    context_object_name = 'articles'
    paginate_by = 20
    date_field = 'posted_at'
    allow_empty = True


class Search(generic.ListView):
    model = models.Article
    context_object_name = 'articles'
    paginate_by = 20
    allow_empty = True

    def get_queryset(self):
        qs = super(Search, self).get_queryset()
        search = self.request.GET.get('q', '').strip()
        if search:
            qs = qs.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search) |
                Q(tags__name__icontains=search)
            ).distinct()
        self.extra_context = {'search': search}
        return qs
