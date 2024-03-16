from django.contrib import admin

from .models import Document

# Регистрация модели в админке
admin.site.register(Document)