from django.contrib import admin

# Register your models here.
from .models import Question, Comment, Poll, PollComment

# this registers Question -- so Django knows that
# it should be displayed on the admin index page
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Poll)
admin.site.register(PollComment)
