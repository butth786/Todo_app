from django.contrib import admin
from django.urls import path ,include
from todo_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todo_app.urls')),
]
