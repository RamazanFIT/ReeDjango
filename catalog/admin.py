from django.contrib import admin


from .models import Catalog

# Регистрация модели в админке
admin.site.register(Catalog)