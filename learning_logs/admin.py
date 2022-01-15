from django.contrib import admin
from learning_logs.models import Topic, Entry

# Register your models here.

admin.site.register(Topic)                                                      # Allows us to manage our model (Topic) through the admin site
admin.site.register(Entry)