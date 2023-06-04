from .views import *
from django.urls import path

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', handleLogin, name='handleLogin'),
    path('logout/', handleLogout, name='handleLogout'),

]