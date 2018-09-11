from django.contrib import admin
from .models import Rightnow


class RightnowAdmin(admin.ModelAdmin):
    model = Rightnow
    list_display = ('content', 'mood', 'status', 'created', 'language')
    list_filter = ['status', 'language']
    search_fields = ['content', 'mood']

admin.site.register(Rightnow, RightnowAdmin)