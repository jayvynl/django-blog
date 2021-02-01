"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from share.views import set_timezone, Index, AboutMe
from django.views.i18n import set_language


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('aubou_me/', AboutMe.as_view(), name='about-me'),
    path('settz/', set_timezone, name='set_timezone'),
    path('setlang/', set_language, name='set_language'),
    path('article/', include('article.urls')),
    path('markdownx/', include('markdownx.urls'))
]
