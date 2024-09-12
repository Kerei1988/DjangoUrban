from django.urls import path
from .views import *

app_name = 'task4'

urlpatterns = (
    path('platform/', platform),
    path('games/', games),
    path('cart/', cart)
)