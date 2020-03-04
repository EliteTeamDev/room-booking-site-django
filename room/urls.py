from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('admin_home/', views.admin_home, name="a_home"),
	path('welcome/', views.welcome_cst, name="welcome"),
	path('signup/', views.new_user, name="signup"),
	path('login/', views.login, name="login"),
	path('auth/', views.home, name="auth"),
	path('rmsignup/', views.new_manager, name="rmsignup"),
	path('customer_home/', views.cust_homepage, name="c_home"),
	
	path('rmwelcome/', views.rm_welcome, name="rmwelcome"),
	path('rmlogin/',views.rm_login, name="rmlogin"),
	path('rmauth/', views.rmhome, name="rmauth"),
	path('rm_home/', views.rm_homepage, name="rm_home"),
	path('rmpanel/', views.rm_panel, name="rmpanel")
]