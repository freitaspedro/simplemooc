# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_reply_thread'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='slug',
            field=models.SlugField(default=-1, unique=True, max_length=100, verbose_name='Atalho'),
            preserve_default=False,
        ),
    ]
