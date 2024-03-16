from rest_framework import routers
from django.urls import include, path
from .views import CatalogViewSet


urlpatterns = [
    path('all/', CatalogViewSet.as_view({'get': 'get_all_catalogs'}), name="doc"),
    path('catalog/<int:pk>', CatalogViewSet.as_view({'get': 'get_catalog'}), name="doc"),
    path('delete/<int:pk>', CatalogViewSet.as_view({'delete': 'delete_catalog'}), name="doc"),
    path('change/', CatalogViewSet.as_view({'patch': 'change_catalog'}), name="doc"),
    path('add/', CatalogViewSet.as_view({'post': 'add_catalog'}), name="doc"),
]