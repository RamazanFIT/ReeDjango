from rest_framework import routers
from django.urls import include, path
from .views import DocumentViewSet

app_name = 'aboutdoc'


urlpatterns = [

    path('all/', DocumentViewSet.as_view({'get': 'get_all_documents'}), name="doc"),
    path('document/<int:pk>', DocumentViewSet.as_view({'get': 'get_document'}), name="doc"),
    path('delete/<int:pk>', DocumentViewSet.as_view({'post': 'delete_document'}), name="doc"),
    path('change/', DocumentViewSet.as_view({'post': 'change_document'}), name="doc"),
    path('add/', DocumentViewSet.as_view({'post': 'add_document'}), name="doc"),
    
]
