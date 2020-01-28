# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-09 03:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmarks',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=200)),
                ('likes', models.PositiveIntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('like', models.BooleanField(default=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('ParentComment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('numCom', models.IntegerField(default=0)),
                ('typeContent', models.CharField(choices=[('post', 'post'), ('video', 'video'), ('qpost', 'qpost'), ('photo', 'photo')], max_length=5)),
                ('preview', models.BooleanField(default=False)),
                ('shared', models.BooleanField(default=False)),
                ('follower_sharable', models.BooleanField(default=False)),
                ('follower_sharable_limit', models.PositiveIntegerField(default=0)),
                ('likesDisabled', models.BooleanField(default=False)),
                ('commentsDisabled', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContentShareRequest',
            fields=[
                ('accept', models.BooleanField(default=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Content')),
                ('userFrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cs_requester', to=settings.AUTH_USER_MODEL)),
                ('userTo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cs_requested', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='FeedObject',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cuuid', models.UUIDField(editable=False)),
                ('type', models.CharField(choices=[('post', 'post'), ('video', 'video'), ('qpost', 'qpost'), ('photo', 'photo')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('like', models.BooleanField(default=True)),
                ('ParentContent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Content')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(max_length=255, null=True)),
                ('content', models.ManyToManyField(to='content.Content')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255, null=True)),
                ('content_meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='p_content_data', to='content.Content')),
            ],
        ),
        migrations.CreateModel(
            name='QPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qpost', models.CharField(max_length=200)),
                ('content_meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='qp_content_data', to='content.Content')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255, null=True)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='')),
                ('content_meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='v_content_data', to='content.Content')),
            ],
        ),
        migrations.AddField(
            model_name='feed',
            name='payloads',
            field=models.ManyToManyField(to='content.FeedObject'),
        ),
        migrations.AddField(
            model_name='feed',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='ParentContent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.Content'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookmarks',
            name='payloads',
            field=models.ManyToManyField(to='content.FeedObject'),
        ),
        migrations.AddField(
            model_name='bookmarks',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
