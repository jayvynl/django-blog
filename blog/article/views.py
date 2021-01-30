from django.views import generic
from article import models
from django.http import Http404


class ArticleList(generic.ListView):
    model = models.Article
    context_object_name = 'articles'
    paginate_by = 20


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

    def get_queryset(self):
        try:
            self.tag = models.Tag.objects.get(pk=self.kwargs['pk'])
        except models.Tag.DoesNotExist:
            raise Http404
        self.queryset = self.tag.articles.all()
        return super().get_queryset()

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(TagDetail, self).get_context_data(object_list=object_list, **kwargs)
        data.update(
            tag=self.tag
        )
        return data
