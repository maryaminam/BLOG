from django.urls import path,include
from .views import UserRegView,UserEditView,PasswordsChangeView,ShowProfilePageView,EditProfilePageView,CreateProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',UserRegView.as_view(), name='register'),
    path('edit_profile/',UserEditView.as_view(), name='edit_profile'),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/profile',ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page',EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page',CreateProfilePageView.as_view(), name='create_profile_page'),
]
