from django.conf.urls import url

from . import views

# Django uses URLconfs -- this maps URL patterns to views

# add this so that if some models have also an index page, Django doesn't get confused as to which index page these urls refer to. Adding app_name ensures that we're calling the index in the polls/views.py
app_name = 'polls'
urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    # /polls/
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # pass in pk instead of question_id when using generic in views
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # /polls/5/vote/
    # browser will run detail() method and display whatever ID you provide in the results
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
