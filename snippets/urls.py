from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9a-zA-Z]+)$', views.snippet_detail),
    url(r'^systemsummary/(?P<pk>[0-9a-zA-Z]+)$', views.systemsummary),
    url(r'^systemstates/(?P<pk>[0-9a-zA-Z]+)$', views.systemstates),
]

urlpatterns = format_suffix_patterns(urlpatterns)