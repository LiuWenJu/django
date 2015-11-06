from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^form', 'west.views.form'),
                       url(r'^investigate', 'west.views.investigate'),
                       url(r'^templay', 'west.views.templay'),
)
