# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_lesson_material'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name_plural': 'Materiais', 'verbose_name': 'Material'},
        ),
    ]
