from rest_framework import routers
from django.urls import include, path
from .views import NewsViewSet




urlpatterns = [

    path('all/', NewsViewSet.as_view({'get': 'get_all_news'}), name="doc"),
    path('news/<int:id>/', NewsViewSet.as_view({'get': 'get_new'}), name="doc"),
    path('additional_photo/<int:id>/', NewsViewSet.as_view({'get': 'get_new_additional_images'}), name="doc"),
    path('news/add', NewsViewSet.as_view({'post': 'create_new'}), name="doc"),
    path('delete/<int:id>/', NewsViewSet.as_view({'delete': 'delete_new'}), name="doc"),
    path('additional_photo/add', NewsViewSet.as_view({'post': 'add_additional_photo'}), name="doc"),
    path('additional_photo/delete/<int:id>/', NewsViewSet.as_view({'delete': 'delete_additional_photo'}), name="doc"),
    path('news/change', NewsViewSet.as_view({'put': 'change_new'}), name="doc"),
    path('additional_photo/change', NewsViewSet.as_view({'put': 'change_additional_photo'}), name="doc"),

]

