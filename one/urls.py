from django.urls import path
from . import views
urlpatterns = [
    path('', views.sendmail,name='home'),
    path('changepass/', views.passwordChangeForm,name='passwordChangeForm'),

    path('register/', views.register,name='register'),
]