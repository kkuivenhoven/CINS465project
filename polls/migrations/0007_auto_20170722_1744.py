# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
