from django.conf.urls import url
from .views import UserListAPIView, CurrentUserView

app_name = "accounts"

urlpatterns = [
	url(r'^users$', UserListAPIView.as_view(), name="users"),
	url(r'^current$', CurrentUserView.as_view(), name="current")
]