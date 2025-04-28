from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_register_view, next_page_view

urlpatterns = [
    path('', login_register_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('next_page/', next_page_view, name='next-page'),
]