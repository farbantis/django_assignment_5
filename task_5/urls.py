from django.urls import path
from.views import index, accept, deny, logout_user, login_user, register_user, change_password, home

app_name = 'task_5'

urlpatterns = [
    path('', index, name='index'),
    path('accept/', accept, name='accept'),
    path('deny/', deny, name='deny'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('home_page/', home, name='home'),
    path('register/', register_user, name='register'),
    path('change_password', change_password, name='change_password')

]
