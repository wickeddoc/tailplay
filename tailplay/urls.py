"""tailplay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

import theme.views
import chats.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", theme.views.SplashView.as_view(), name="index"),
    path("queue", theme.views.QueueView.as_view(), name="queue"),
    path("chat", chats.views.ChatView.as_view(), name="chat"),
    # login-section
    path("login", LoginView.as_view(template_name="chats/login.html"), name="login-user"),
    path("logout", LogoutView.as_view(), name="logout-user"),

]