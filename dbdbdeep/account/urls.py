from django.urls import path
from . import views

urlpatterns = [
    path('', views.signUp, name='signUp'),
    path('signIn/',views.signIn, name='SignIn'),
    path('doSignUp/',views.doSignUp, name='doSignUp'),
    path('signIn/doSignIn/',views.doSignIn, name='doSignIn'),
]