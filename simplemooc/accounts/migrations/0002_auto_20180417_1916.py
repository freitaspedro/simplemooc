# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import re


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('key', models.CharField(verbose_name='Chave', unique=True, max_length=100)),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False, verbose_name='Confirmado')),
            ],
            options={
                'verbose_name_plural': 'Novas Senhas',
                'verbose_name': 'Nova Senha',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário só pode conter letras, dígitos ou os seguintes caracteres: @/./+/-/_', 'invalid')], verbose_name='Nome de Usuário', unique=True, max_length=30),
        ),
        migrations.AddField(
            model_name='passwordreset',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]
