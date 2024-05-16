from django.urls import path
from .views import *


urlpatterns = [
    path('',homePage,name="home"),
    path('checkout',test,name="checkout"),
    path('callback',callback,name="callBack")
]