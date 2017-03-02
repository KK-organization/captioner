from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$',views.signinpage),
    url(r'^home/', views.homepage, name="home"),
    url(r'^signupattempt/', views.signup_attempt),
    url(r'^signinattempt/', views.signin_attempt),
    url(r'^signin/',views.signinpage),
    url(r'^signup/',views.signuppage),
]