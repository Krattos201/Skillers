
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('About/', views.about, name='about'),
	path('Register_form',views.Register_form, name='Register_form'),
	path('Enter_otp/', views.Enter_otp, name='Enter_otp'),
	path('Otp_validation',views.Otp_validation, name='Otp_validation'),
	path('redirect',views.redirect,name='redirect'),

]
