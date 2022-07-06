from blog.models import Article, Category


# --- blog sidebar ---
def mostVisitedArticle(request):
    most_visited_article = Article.objects.all().order_by('-view')[:2]
    return {'most_visited_article': most_visited_article}

def showCategorySidebar(request):
    categories = Category.objects.all()[:3]
    return {'categories': categories}
# --- end blog sidebar ---     