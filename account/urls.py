
from django.urls import path

from user_app.views import identifyUser

from .views import login_view, logout_view, register_view,index

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
]