from django.urls import path
from . import views


app_name = 'ImagePurger'

urlpatterns = [
    path('', views.purge, name='purge'),
]
