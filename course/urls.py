from django.urls import path
from .views import RegisterView, login_view, success_view, logout_view

urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('courses/', RegisterView, name='courses'),
    path('login/', login_view, name='login'),
    path('success/', success_view, name='success'),
    path('logout/', logout_view, name='logout'),
]
