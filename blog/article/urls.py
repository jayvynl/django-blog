from django.urls import path
from article import views

app_name = 'article'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
    path('tag/', views.TagList.as_view(), name='tag-list'),
    path('tag/<int:pk>/', views.TagDetail.as_view(), name='tag-detail'),
    path('archive/', views.ArchiveIndex.as_view(), name='archive'),
    path('archive/<int:year>/', views.YearArchive.as_view(), name='year-archive'),
    path('search/', views.Search.as_view(), name='search'),
]
