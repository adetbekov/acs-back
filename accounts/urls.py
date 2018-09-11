from django.urls import path
import accounts.views
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

urlpatterns = [
	path('login', obtain_jwt_token),
	path('refresh', refresh_jwt_token)
]