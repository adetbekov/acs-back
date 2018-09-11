from rightnow.models import Rightnow
from rest_framework import serializers


class RightnowSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rightnow
		fields = ['content', 'mood', 'created']