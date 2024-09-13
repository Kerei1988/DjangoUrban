from django.urls import path
from .views import sign_up_by_django, sign_up_by_html

app_name= 'task5'

urlpatterns = [
    path('django_sign_up/', sign_up_by_django),
    path('', sign_up_by_html)
]