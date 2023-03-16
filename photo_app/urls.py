from django.urls import path
from photo_app import views

urlpatterns = [
    path('', views.index, name='index')
]
