from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

# Имена маршрутов (register, login, logout) оставлены прежними,
# чтобы не ломать {% url %} в шаблонах.
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
