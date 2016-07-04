# encoding: utf-8

"""
Definition of urls for webui.
"""

# Serving files uploaded by a user during development
# REF: https://docs.djangoproject.com/en/1.8/howto/static-files/#serving-files-uploaded-by-a-user-during-development 

from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import patterns, url, include
from webui import views


urlpatterns = patterns('',
    url(r'^$', views.SearchLogView.as_view(), name='serverLog-list'),


)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)