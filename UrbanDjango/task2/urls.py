
from django.urls import path
from .views import class_view, func_view

app_name = 'task2'

urlpatterns = [
    path('class/', class_view, name='class'),
    path('func/', func_view, name='func')
]