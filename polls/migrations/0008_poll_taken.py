# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20170722_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='taken',
            field=models.IntegerField(default=0),
        ),
    ]
