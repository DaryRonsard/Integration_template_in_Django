from django.contrib import admin
from django.urls import path
from teacher.views import index

app_name = 'teacher'
urlpatterns = [
    path('', index, name='index'),
]