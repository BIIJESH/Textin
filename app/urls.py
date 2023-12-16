
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('retreat/', views.retreat, name="retreat"),
    path('inventory/', views.inventory, name="inventory"),
    path('post/',views.post, name="post"),
    path('login/',views.sign_up, name='login'),
    path('register/',views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    

]
