# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(related_name='replies', default=-1, to='forum.Thread', verbose_name='Tópico'),
            preserve_default=False,
        ),
    ]
