from django.urls import path
from tempapp01 import views

# Template tagging
app_name = 'tempapp01'

urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),


]
