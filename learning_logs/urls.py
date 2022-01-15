"""Define URL patterns for learning_logs."""

from django.urls import path                                                                        # Needed to map URLs to views
from . import views
app_name = 'learning_logs'

                                                                                                    # Must include the name of the app as specified by the namespace in the root URL

urlpatterns = [                                                                                     # A list of individual pages that can be requested from the learning_logs app

    path('', views.index, name='index'),                                                            # url is a function that takes in three arguments:
                                                                                                    # The first is a regular expression. Django matches this express with a URL string. 'r' means interpert as raw string, quotes is where expression begins/ends, ^ means beginning of string, and $ sign tells python to look for the end of the string
                                                                                                    # Second one species which view function to call.. in this instance it will call views.index
                                                                                                    # Third one is so we can reference this URL pattern in other sections of code
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
]