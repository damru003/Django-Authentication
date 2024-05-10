from django.contrib import admin
from django.urls import path
from login_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.login, name='home'),
    path("login", views.login, name='login'),
    path("signup", views.signup, name='signup'),
    path ("home", views.home, name='home')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

