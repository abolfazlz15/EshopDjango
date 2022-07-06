from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
# from extensions.utils import jalali_converter


class Category(models.Model):
    name = models.CharField(max_length=155, verbose_name='نام ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')
    updated = models.TimeField(auto_now=True, verbose_name='زمان بروزرسانی')
    slug = models.SlugField(blank=True, null=True, verbose_name='اسلاگ')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(Category, self).save()

    # def get_absolute_url(self):
    #     return reverse('blog:details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=155, verbose_name='عنوان مقاله')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده', related_name='articles')
    description = RichTextField(verbose_name='توضیحات')
    category = models.ManyToManyField(Category, related_name='articles', verbose_name='دسته بندی ها')
    tag = models.ManyToManyField(Tag, related_name='articles', verbose_name='برچسب ها')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    published = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی')
    slug = models.SlugField(blank=True, null=True, verbose_name='اسلاگ')
    image = models.ImageField(verbose_name='تصویر')
    status = models.BooleanField(default=0, verbose_name='وضعیت')
    view = models.IntegerField(default=0, verbose_name='تعداد بزدید ها')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ('-created_date',)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.title} - {self.description[:30]}'

    def j_publish(self):
        time = timezone.localtime(self.created_date)
        return time


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='کاربر')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies',
                               verbose_name='زیر مجموعه')
    body = models.TextField(verbose_name='متن')
    email = models.EmailField(verbose_name='ایمیل', null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'

    def __str__(self):
        return f'{self.article} - {self.user} - {self.body[:30]}'

    def j_publish(self):
        time = timezone.localtime(self.created_at)
        return time
