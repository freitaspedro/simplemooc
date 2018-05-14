# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_auto_20180418_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('status', models.IntegerField(default=1, blank=True, verbose_name='Situação', choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')])),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('course', models.ForeignKey(verbose_name='Curso', to='courses.Course', related_name='enrollements')),
                ('user', models.ForeignKey(verbose_name='Usuário', to=settings.AUTH_USER_MODEL, related_name='enrollements')),
            ],
            options={
                'verbose_name': 'Inscrição',
                'verbose_name_plural': 'Inscrições',
            },
        ),
        migrations.AlterUniqueTogether(
            name='enrollement',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='enrollement',
            name='course',
        ),
        migrations.RemoveField(
            model_name='enrollement',
            name='user',
        ),
        migrations.DeleteModel(
            name='Enrollement',
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('user', 'course')]),
        ),
    ]
