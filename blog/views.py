from django.shortcuts import render, get_object_or_404
from .models import Article, Comment, Category, Tag
from django.core.paginator import Paginator
from .forms import CommentFrom
from django.contrib.auth.models import User


def articleList(request):
    articles = Article.objects.filter(status=True).order_by('-published')
    paginator = Paginator(articles, 3)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    context = {
        'articles': articles,
    }
    return render(request, 'blog/article_list.html', context)


def articleDetail(request, slug):
    article = get_object_or_404(Article.objects.filter(status=True), slug=slug)  # get object from database
    count_of_comment_article = article.comments.count()  # getting number of comments
    
    if request.method == 'POST':
        form = CommentFrom(data=request.POST)
        if form.is_valid():
            body = form.cleaned_data.get('body')
            email = form.cleaned_data.get('email')
            parent_id = request.POST.get('parent_id')
            Comment.objects.create(parent_id=parent_id, user=request.user, article=article, body=body, email=email)

    else:
        form = CommentFrom()  # if request type == GET sending null from
    context = {
        'articles': article,
        'count_of_comment_article': count_of_comment_article,
        'form': form,
    }
    return render(request, 'blog/article_details.html', context)


def authorList(request, username):
    author = get_object_or_404(User, username=username)
    categories = Category.objects.all()
    articles = author.articles.filter(status=True)
    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    context = {
        'articles': articles,
        'categories': categories,
    }
    return render(request, 'blog/article_list.html', context)


def categoryList(request, slug):
    category = get_object_or_404(Category, slug=slug)
    categories = Category.objects.all()
    articles = category.articles.filter(status=True)
    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    context = {
        'articles': articles,
        'categories': categories,
    }
    return render(request, 'blog/article_list.html', context)
