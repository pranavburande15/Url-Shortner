from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:pk>/', views.update_url, name='update_url'),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
]