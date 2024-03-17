from rest_framework import routers
from django.urls import include, path
from .views import MessageViewSet




urlpatterns = [

    path('all/', MessageViewSet.as_view({'get': 'get_all_message'}), name="doc"),
    path('get/<int:id>/', MessageViewSet.as_view({'get': 'get_message'}), name="doc"),
    path('delete/<int:id>/', MessageViewSet.as_view({'delete': 'delete_message'}), name="doc"),
    path('add/', MessageViewSet.as_view({'post': 'add_message'}), name="doc"),
    path('change/<int:id>', MessageViewSet.as_view({'put': 'change_message'}), name="doc"),
    
]

