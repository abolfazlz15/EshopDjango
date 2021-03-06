# Generated by Django 4.0.4 on 2022-07-02 18:10

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='عنوان مقاله')),
                ('description', ckeditor.fields.RichTextField(verbose_name='توضیحات')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('created_time', models.TimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_date', models.DateField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('update_time', models.TimeField(auto_now=True, verbose_name='زمان بروزرسانی')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='اسلاگ')),
                ('image', models.ImageField(upload_to='', verbose_name='تصویر')),
                ('status', models.BooleanField(default=0, verbose_name='وضعیت')),
                ('view', models.IntegerField(default=0, verbose_name='تعداد بزدید ها')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='نویسنده')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
                'ordering': ('-created_date', '-created_time'),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155, verbose_name='نام ')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='زمان ساخت')),
                ('updated', models.TimeField(auto_now=True, verbose_name='زمان بروزرسانی')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='اسلاگ')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='')),
                ('created', models.DateField(auto_now_add=True, verbose_name='')),
                ('publish', models.DateTimeField(auto_now=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'برچسب',
                'verbose_name_plural': 'برچسب ها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='متن')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.article', verbose_name='مقاله')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comment', verbose_name='زیر مجموعه')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنت ها',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='blog.category', verbose_name='دسته بندی ها'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='articles', to='blog.tag', verbose_name='برچسب ها'),
        ),
    ]
