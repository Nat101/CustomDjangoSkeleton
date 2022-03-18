from django.urls import path
from . import views

urlpatterns = [
	path('Home', views.Home, name='Home'),

	path('GeneralAccess', views.GeneralAccess, name='GeneralAccess'),
	path('RestrictedAccessA', views.RestrictedAccessA, name='RestrictedAccessA'),
	path('RestrictedAccessB', views.RestrictedAccessB, name='RestrictedAccessB'),
	path('RestrictedAccessC', views.RestrictedAccessC, name='RestrictedAccessC'),
	
]