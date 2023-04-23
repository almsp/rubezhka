from django.urls import path, include
from volunteers.views import volunteers, user_login, user_logout, register

urlpatterns = [
    path('volunteers/', volunteers, name='volunteers'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='logout')
]
