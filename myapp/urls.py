from django.urls import path, include
from . import views
import uuid
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

admin.site.site_header = "Site-Header"
admin.site.site_title = "Side-Title"
admin.site.index_title = "Welcome to MySite"
