from django.shortcuts import redirect
from django.views import generic
from article.models import Article
from share.models import PersonalInfo


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        redirect_to = request.POST.get('next', '/')
        return redirect(redirect_to)


class Index(generic.ListView):
    queryset = Article.objects.all()[:10]
    context_object_name = 'articles'
    template_name = 'index.html'


class AboutMe(generic.DetailView):
    template_name = 'about_me.html'
    context_object_name = 'personal_info'

    def get_object(self, queryset=None):
        try:
            return PersonalInfo.objects.first()
        except PersonalInfo.DoesNotExist:
            return None
