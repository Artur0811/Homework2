from django.urls import path

from WEBAstro.views import *

urlpatterns = [
    path("", main_page, name = "home"),
    path("about/", About,name = "about"),
    path("user/", User, name = "user_page"),
    path("login/", LoginUser.as_view(), name = "login_page"),
    path("register/", RegisterUser.as_view(), name = "register"),
    path("AstroAssistant/", AstroAssistant ,name = "astroassistant"),
]
