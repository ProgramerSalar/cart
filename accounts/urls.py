from django.urls import path 
from . import views

urlpatterns = [
    path('register/' , views.register , name = 'register'),
    path('login/' , views.login , name='login'),
    path('logout/', views.logout , name = 'logout'),
    path('deshboard/' , views.deshboard , name = 'deshboard'),
    path('' , views.deshboard , name = 'deshboard'),
    path('forgotPassword/', views.forgotPassword , name = 'forgotPassword'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
]
