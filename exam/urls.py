
from django.urls import path

from . import views


app_name='exam'

urlpatterns = [
	path('',views.exam,name = 'exam'),
	 
]
# Create your views here.
