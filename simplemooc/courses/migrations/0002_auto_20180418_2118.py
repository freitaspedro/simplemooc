# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=0, blank=True, choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], verbose_name='Situação')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('course', models.ForeignKey(to='courses.Course', verbose_name='Curso', related_name='enrollements')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='enrollements')),
            ],
            options={
                'verbose_name_plural': 'Inscrições',
                'verbose_name': 'Inscrição',
            },
        ),
        migrations.AlterUniqueTogether(
            name='enrollement',
            unique_together=set([('user', 'course')]),
        ),
    ]
