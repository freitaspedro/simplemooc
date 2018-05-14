# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='Nome de Usuário', unique=True, max_length=30)),
                ('email', models.EmailField(verbose_name='E-mail', unique=True, max_length=254)),
                ('name', models.CharField(verbose_name='Nome', max_length=100, blank=True)),
                ('is_active', models.BooleanField(verbose_name='Ativo', default=True)),
                ('is_staff', models.BooleanField(verbose_name='Staff', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='Data de Entrada', auto_now_add=True)),
                ('groups', models.ManyToManyField(related_name='user_set', to='auth.Group', related_query_name='user', verbose_name='groups', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', to='auth.Permission', related_query_name='user', verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
