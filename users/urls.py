from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views import generic

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='google_login'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(), name="logout"),
    path('<int:pk>/profile/', views.UserProfileView.as_view(), name='profile'),
    path('<int:pk>/custom_js.js/', views.CustomJs.as_view(), name='custom_js'),
]