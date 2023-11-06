from django.urls import path
from menu.views import *

app_name = 'menu'

urlpatterns = [
    path('nav_menu/', IndexPageView.as_view(), name='index')
]