from django.contrib import admin
from django.urls import path

from .views import home_view ,score_view

urlpatterns=[
	path('',home_view,name='home'),
	path('scores/<int:unique_id>',score_view,name='scores')
]