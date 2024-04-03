from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('country/<slug:slug>/', views.get_country),
    path('countries-list/', views.country_list)
]