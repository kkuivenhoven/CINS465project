# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0008_poll_taken'),
    ]

    operations = [
        migrations.CreateModel(
            name='PollComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
                ('poll', models.ForeignKey(to='polls.Poll')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
