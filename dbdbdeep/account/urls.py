from django.urls import path
from . import views

urlpatterns = [
    path('', views.signUp, name='signUp'),
    path('doSignUp/',views.doSignUp, name='doSignUp'),
]