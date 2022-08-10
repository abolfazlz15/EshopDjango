from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class Brand(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='نام')
    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title


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


class Product(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, null=True, verbose_name='اسلاگ')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='انتشار دهنده', related_name='products')
    category = models.ManyToManyField(Category, related_name='products', verbose_name='دسته بندی ها')
    tag = models.ManyToManyField(Tag, related_name='products', verbose_name='برچسب ها')
    description = RichTextField(verbose_name='توضیحات')
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='product/image')
    brand = models.ForeignKey(Brand, default='برند ندارد', on_delete=models.SET_DEFAULT)
    status = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ('-created',)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Product, self).save()

    # def get_absolute_url(self):
    #     return reverse('blog:article_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment', verbose_name='محصول')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment', verbose_name='کاربر')
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
