from django.db import connection
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView

from menu.models import *

from django.shortcuts import render


class IndexPageView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['menu'] = Menu.objects.filter(slug='root').first()
        return context
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        response = super().get(request, *args, **kwargs)
        print("Number of database queries: ", len(connection.queries))
        return response


