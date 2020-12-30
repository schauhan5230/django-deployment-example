#from django.conf.urls import url
from django.urls import path
from django.conf.urls import url
from basic_appt import views

#TEMPLATE TAGGING
app_name = 'basic_appt'

urlpatterns = [
    #path('',                           views.index,    name='index'),
    url(r'^relative/$',                 views.relative, name='relative'),
    #path('basic_appt/relative/',       views.relative, name='relative'),
    url(r'^other/$',                    views.other,    name='other'),
    #path('basic_appt/other/',          views.other,    name='other'),
]
