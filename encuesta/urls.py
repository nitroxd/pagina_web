from django.conf.urls import patterns, include, url
from django.contrib import admin
from encuesta import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.volver, name='volver'),
    # ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^lista_preguntas/$', views.index, name='index'),
    url(r'^lista_preguntas1/$', views.indice, name='indice'),
)