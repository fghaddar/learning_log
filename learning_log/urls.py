"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin                                                    # This import and the other below import the functions/modules that manage the URLS for the project and admin site
#from django.conf.urls import include, url                                          # url is deprecated, use path instead (found in import below) 
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns                 # For static files and images: Lets us append to urlpatterns so that django can handle the serving up of statis files


urlpatterns = [                                                                     # A set of URLs that can be requested from the admin site
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls', namespace='learning_logs')),             # Include the module learning_logs.urls, and name it learning_logs to distinguish it from other URL's        
    path('users/', include('users.urls', namespace='users')),
]

urlpatterns += staticfiles_urlpatterns()                                            # For static files and images: Append static files to urlpatterns so that urlpatterns knows how to serve the files