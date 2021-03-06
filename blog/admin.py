from django.contrib import admin
from .models import Category, Article, Tag, Comment

# admin header change
admin.site.site_header = 'پنل مدیریت سایت ای شاپ'

admin.site.register(Category)
admin.site.register(Tag)

class CommentInLine(admin.StackedInline): # for show comment in article detail (Django admin panel)
    model = Comment
    
@admin.register(Article)
class ArticleAdminModel(admin.ModelAdmin):
    fields = ('title', 'author', 'tag', 'category','description', 'published', 'slug', 'image', 'view')
    list_display = ('showImage', 'title', 'status', 'author', 'view')
    list_display_links = ('showImage', 'title')
    list_filter = ('status', 'created_date')
    search_fields = ['category__name', 'title', 'description']
    inlines = (CommentInLine,)
    actions = ['enableStatus', 'disableStatus']


    # actions articles
    @admin.action(description='مقالات انتخب شده وضعیتاشان فعال میشود')
    def enableStatus(self, request, queryset):
        queryset.update(status=True)

    @admin.action(description='مقالات انتخب شده وضعیتاشان غیر فعال میشود')
    def disableStatus(self, request, queryset):
        queryset.update(status=False)    

@admin.register(Comment)
class ArticleCommentAdminModel(admin.ModelAdmin):
    list_display = ('user', 'article', 'status', 'created_at')
    search_fields = ['user']
    list_filter = ('status', 'created_at')
