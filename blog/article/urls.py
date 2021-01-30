from django.urls import path
from article import views

app_name = 'article'

urlpatterns = [
    path('', views.ArticleList.as_view(), name='list'),
    path('<int:pk>/', views.ArticleDetail.as_view(), name='detail'),
    path('tag/', views.TagList.as_view(), name='tag-list'),
    path('tag/<int:pk>/', views.TagDetail.as_view(), name='tag-detail')
]
