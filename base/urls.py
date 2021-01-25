from django.urls import path

from . import views
from .views import LatestPostt


urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', LatestPostt.as_view(), name='latestpost'),

    path('programing/', views.Programing, name='programing'),
    path('tech/', views.Tech, name='tech'),
    path('international/', views.International, name='international'),
   
    path('it/', views.IT, name='it'),

    path('search/', views.Search, name='search'),

    


    ]
