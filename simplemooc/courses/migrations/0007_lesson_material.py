# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20180427_1916'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('description', models.TextField(verbose_name='Descrição', blank=True)),
                ('number', models.IntegerField(verbose_name='Ordem', default=0, blank=True)),
                ('release_date', models.DateField(verbose_name='Data de Liberação', null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('course', models.ForeignKey(verbose_name='Curso', to='courses.Course', related_name='lessons')),
            ],
            options={
                'ordering': ['number'],
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('embedded', models.TextField(verbose_name='Embedded', blank=True)),
                ('file', models.FileField(upload_to='lessons/materials', null=True, blank=True)),
                ('lesson', models.ForeignKey(verbose_name='Aula', to='courses.Lesson', related_name='materials')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Msterials',
            },
        ),
    ]
