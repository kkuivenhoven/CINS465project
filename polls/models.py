import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible #necessary so that in python shell get helpful results back from Question.objects.all()
from django.utils import timezone
# Create your models here.

class Poll(models.Model):
        name = models.CharField(max_length=200)
        taken = models.IntegerField(default=0)
        def __str__(self):
             return self.name

DEFAULT_POLL_ID = 1
# Question has 2 fields
class Question(models.Model):
        poll = models.ForeignKey(Poll, on_delete=models.CASCADE, default=DEFAULT_POLL_ID)
        # CharField has required arg of max_length
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
        def __str__(self):
            return self.question_text
        def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice has 3 fields
class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        choice_text = models.CharField(max_length=200)
        # Field can have optional arguments
        votes = models.IntegerField(default=0)
        def __str__(self):
            return self.choice_text

DEFAULT_USER_ID = 1
# Following this tutorial:
# https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/homework_create_more_models/
class Comment(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        author = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        approved_comment = models.BooleanField(default=False) 
        # user = models.OneToOneField(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)
        user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)

        def approve(self):
            self.approved_comment = True
            self.save()

        def __str__(self):
            return self.text


class PollComment(models.Model):
        poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
        author = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        approved_comment = models.BooleanField(default=False) 
        # user = models.OneToOneField(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)
        user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)

        def approve(self):
            self.approved_comment = True
            self.save()

        def __str__(self):
            return self.text






