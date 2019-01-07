from django.urls import path
from . import views

app_name='country'

urlpatterns=[
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('search/', views.searching, name='search'),
    path('myChart/', views.chart, name='myChart'),
]
