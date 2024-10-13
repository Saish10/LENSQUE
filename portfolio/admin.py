from django.contrib import admin
from .models import Category, Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')
    search_fields = ('title',)
    list_filter = ('category',)

admin.site.register(Category)
admin.site.register(Photo, PhotoAdmin)
