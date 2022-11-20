from django.urls import path

from wakeapp.auth_app.views import UserRegistrationView

urlpatterns = [
    # path('edit/<int:id>/, EditProfileView.as_view', name='edit profile'),
    path('register/', UserRegistrationView.as_view(), name='register'),
]
