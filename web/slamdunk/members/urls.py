from django.urls import path
from . import views

app_name = 'members'
urlpatterns = [
    path('stw/', views.stw, name='stw'),
    path('kbh/', views.kbh, name='kbh'),
]