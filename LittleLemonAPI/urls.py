from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('menu/', views.MenuView.as_view(), name='menu-view'),
    path('booking/', views.BookingView.as_view(), name='booking-view'),
 
]