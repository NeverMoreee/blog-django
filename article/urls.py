from django.conf.urls import url

from . import views

app_name = 'article'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^id/(?P<article_id>[0-9]+)/$', views.article_id, name='article_id'),
    url(r'^type/(?P<article_type>[\W\w]+)/$', views.article_type, name='article_type'),

]

