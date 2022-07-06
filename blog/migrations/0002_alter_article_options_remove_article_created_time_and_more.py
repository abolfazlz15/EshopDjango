# Generated by Django 4.0.4 on 2022-07-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created_date',), 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='article',
            name='update_date',
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, verbose_name='زمان بروزرسانی'),
        ),
    ]
