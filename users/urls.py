"""Defines URL patterns for users"""

from django.urls import path 
from django.contrib.auth.views import LoginView, LogoutView                                 # Import the default login and logout view
from . import views
app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),      # login tells it o send to send requests to Django's defailt login view 
                                                                                            # We are not creating our own view function, so we need to pass a dictionary telling Django where to find the template we're about to write
    
    # path('logout/', views.logout_view , name='logout'),
    path('logout/', LogoutView.as_view(template_name='learning_logs/index.html'), name='logout'),
    path('register/', views.register, name='register'),
]