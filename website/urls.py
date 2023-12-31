
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('customer/<int:pk>/', views.customer_record, name='customer'),
    path('delete_customer/<int:pk>/', views.delete_record, name='delete'),
    path('add_customer/', views.add_record, name='add-record'),
    path('update_customer/<int:pk>/', views.update_record, name='update_record'),
]
