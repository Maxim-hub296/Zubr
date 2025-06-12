from django.urls import path

from . import views

app_name = 'authentication'
urlpatterns = [
    path("registration/", views.CustomRegisterView.as_view(), name="registration"),
    path("login/", views.MyLoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
