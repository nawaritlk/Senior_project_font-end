from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import *
from django.views.static import serve
from django.conf import settings
# app_name = "App_Posts"

admin.autodiscover()

urlpatterns = [
    path("register/", views.register),
    # path("",views.homepage, name= 'homepage'),
    path("authlogin/", views.authlogin, name = 'authlogin'),
    path("logout/", views.authlogout, name = 'authlogout'),
    path("forgetpassword/", views.forgetpassword, name = 'forgetpassword'),
    path("login/", views.login_before, name = 'login'),
    path("", views.profile, name = 'profile'),
    path("delete/<pk>/", views.delete_output, name='delete-output'),
    path("private/<pk>/", views.make_private, name='private'),
    path("public/<pk>/", views.make_public, name='public'),


    #reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="forgetpassword/password_reset_form.html"), name = 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="forgetpassword/password_reset_done.html"), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="forgetpassword/password_reset_confirm.html"), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="forgetpassword/password_reset_complete.html"), name = 'password_reset_complete'),
]
