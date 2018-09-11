from rightnow.models import Rightnow
from rest_framework import serializers


class RightnowSerializer(serializers.ModelSerializer):
	locale_code = serializers.SerializerMethodField()

	class Meta:
		model = Rightnow
		fields = ['content', 'mood', 'locale_code', 'created']

	def get_locale_code(self, obj):
		if obj.language:
			return obj.language.code
		else:
			return 'ru'