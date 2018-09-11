from django.urls import path
from .views import RightnowView

app_name = "rightnow"

urlpatterns = [
	path('all', RightnowView.as_view())
]