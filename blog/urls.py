from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.articleList, name='article_list'),
    path('detail/<slug:slug>', views.articleDetail, name='article_detail'),
    path('author/<str:username>', views.authorList, name='author'),
    path('author/<str:username>/page/<int:page>', views.authorList, name='author'),
    path('category/<slug:slug>', views.categoryList, name='category_list'),
]