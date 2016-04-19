# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 16:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import wagtail.wagtailadmin.taggable
import wagtail.wagtailcore.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('wagtailcore', '0028_merge'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', models.FileField(upload_to='media', verbose_name='file')),
                ('type', models.CharField(choices=[('audio', 'Audio file'), ('video', 'Video file')], max_length=255)),
                ('duration', models.PositiveIntegerField(verbose_name='duration')),
                ('width', models.PositiveIntegerField(blank=True, null=True, verbose_name='width')),
                ('height', models.PositiveIntegerField(blank=True, null=True, verbose_name='height')),
                ('thumbnail', models.FileField(blank=True, upload_to='media_thumbnails', verbose_name='thumbnail')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('collection', models.ForeignKey(default=wagtail.wagtailcore.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Collection', verbose_name='collection')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
                ('uploaded_by_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'media',
            },
            bases=(models.Model, wagtail.wagtailadmin.taggable.TagSearchable),
        ),
    ]
