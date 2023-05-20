from django.urls import path
from user_app.views import identifyUser

from .views import about, contact, featured, index

urlpatterns = [
    path("", index, name="index"),
    path("aboutus", about, name="about"),
    path("contactus", contact, name="contact"),
    path("featured", featured, name="featured"),
    path('dashboard', identifyUser, name="dashboard"),
]

