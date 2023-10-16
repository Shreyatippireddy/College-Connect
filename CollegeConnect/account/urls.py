from django.urls import path
from . import views

urlpatterns= [
    path('register',views.register,name="register"),
    path('login',views.login,name="login"),
    path('profile',views.profile,name="profile"),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('change_password',views.change_password,name="change_password"),

]




