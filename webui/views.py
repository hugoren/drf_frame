# encoding: utf-8
import sys
import simplejson as json
import time
import requests
import logging
from datetime import datetime
from vanilla import ListView
from webui import forms

from framework import  models



logInfo = logging.getLogger('log_info')
logErr = logging.getLogger('log_error')

class SearchLogView(ListView):
    model = models.YMATOULOG
    form_class = forms.SearchLog
    queryset = None
    lookup_field = 'title'
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(SearchLogView, self).get_context_data(**kwargs)

        # add search form
        context['form'] = self.get_form()
        # context['title'] = u'日志系统'
        # context['introduction'] = u'日志系统简介'

        # show maintenance notification. If it's empty, the notification will not be appeared in the page.
        context['notification'] = u''

        # login partial and commons
        context['year'] = datetime.now().year

        return context

    def get_queryset(self):
        # support search
        try:
            app = self.request.GET['app']
            operater = self.request.GET['operater']
        except:
            app = ''

        if app == '':
            return models.YMATOULOG.objects.filter(app=app).order_by('id')
        else:
            return models.YMATOULOG.objects.filter(operater=operater).order_by('id')



