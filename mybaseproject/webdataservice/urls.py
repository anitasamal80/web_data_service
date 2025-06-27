from django.urls import path
from . import views



urlpatterns = [
    
    path('', views.home),    
    path('home/', views.home),    
    path('charts/', views.chartpage),    
    path('signup/', views.signup),    
    
]