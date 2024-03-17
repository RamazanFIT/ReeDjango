from django.contrib import admin

from .models import News, AdditionalPhotosOfNews

# Регистрация модели в админке
admin.site.register(News)
admin.site.register(AdditionalPhotosOfNews)