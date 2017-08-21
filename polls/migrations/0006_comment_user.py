# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0005_question_poll'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.OneToOneField(default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]
