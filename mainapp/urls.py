from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('', views.about, name='about'),
	path('', views.portfolio_details, name='portfolio_details'),

]
