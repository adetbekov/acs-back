from django.contrib import admin
from .models import Category, Tag, Locale

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class LocaleAdmin(admin.ModelAdmin):
	pass

admin.site.register(Locale, LocaleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)