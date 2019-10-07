from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', authViews.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(template_name='account/login.html'), name='logout'),
]
