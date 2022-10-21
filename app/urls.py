from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('likes',views.likes,name='likes'),
    path('createEvent',views.createEvent,name='createEvent'),
]