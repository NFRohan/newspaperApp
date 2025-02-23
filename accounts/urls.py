from django.urls import path
from .views import SignUpView

urlpatterns = [
    # Add your URL patterns here
    path('signup/', SignUpView.as_view(), name='signup'),
]