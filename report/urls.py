from django.urls import path

from report.views import index

app_name = 'report'
urlpatterns = [
    path('', index, name='index'),
]