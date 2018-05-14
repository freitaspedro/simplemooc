# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_announcement_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='course',
            field=models.ForeignKey(verbose_name='Curso', to='courses.Course', related_name='announcements'),
        ),
    ]
