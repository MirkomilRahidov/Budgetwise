from django.urls import path
from .views import RegisterView,LoginView,LogoutView,ProfileView,profileupdate
from .views_api import RegisterAPI, LoginAPI, LogoutAPI, ProfileAPI
app_name='users'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', profileupdate, name='profile_update'),
    path('api/register/', RegisterAPI.as_view(), name='api_register'),
    path('api/login/', LoginAPI.as_view(), name='api_login'),
    path('api/logout/', LogoutAPI.as_view(), name='api_logout'),
    path('api/profile/', ProfileAPI.as_view(), name='api_profile'),
]
