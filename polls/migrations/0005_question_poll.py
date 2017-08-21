# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='poll',
            field=models.ForeignKey(default=1, to='polls.Poll'),
        ),
    ]
