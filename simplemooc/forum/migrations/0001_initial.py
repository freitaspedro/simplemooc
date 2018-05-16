# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(verbose_name='Correta', default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('author', models.ForeignKey(related_name='replies', verbose_name='Autor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-correct', 'created_at'],
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('body', models.TextField(verbose_name='Mensagem')),
                ('views', models.IntegerField(blank=True, verbose_name='Visualizações', default=0)),
                ('answers', models.IntegerField(blank=True, verbose_name='Respostas', default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('author', models.ForeignKey(related_name='threads', verbose_name='Autor', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', to='taggit.Tag', help_text='A comma-separated list of tags.')),
            ],
            options={
                'ordering': ['-updated_at'],
                'verbose_name': 'Tópico',
                'verbose_name_plural': 'Tópicos',
            },
        ),
    ]
