from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('response/', views.response),
    path('chatbot/', views.chatbot, name='chatbot'),

]
