from django.urls import path
from wakeapp.main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='dashboard'),
]
