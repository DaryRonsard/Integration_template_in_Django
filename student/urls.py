from django.contrib import admin
from django.urls import path

from student.views import index, add, edit

app_name = 'student'
urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add'),
    path('edit/', edit, name='edit'),
]