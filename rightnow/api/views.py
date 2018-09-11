from rightnow.models import Rightnow
from .serializers import RightnowSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny


class RightnowView(ListAPIView):
	queryset = Rightnow.objects.filter(status='P').order_by('-created')
	permission_classes = (AllowAny,)
	serializer_class = RightnowSerializer
