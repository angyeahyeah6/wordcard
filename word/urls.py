from django.urls import path

from . import views


app_name='word'

urlpatterns = [
	path('',views.index,name = 'index'),
	path('phrase/',views.phrase,name = 'phrase'),
]