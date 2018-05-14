# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20180418_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrollment',
            name='course',
            field=models.ForeignKey(to='courses.Course', related_name='enrollments', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='enrollments', verbose_name='Usuário'),
        ),
    ]
