from django.shortcuts import redirect
from django.views import generic
from article import models


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        redirect_to = request.POST.get('next', '/')
        return redirect(redirect_to)


class Index(generic.ListView):
    model = models.Article.objects.all()[:10]
    context_object_name = 'articles'
    template_name = 'index.html'
