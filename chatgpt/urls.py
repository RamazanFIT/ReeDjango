from rest_framework import routers
from django.urls import include, path
from .views import ChatGptViewSet

app_name = 'chatgpt'


urlpatterns = [

    path('chatgpt/', ChatGptViewSet.as_view({'post': 'get_chatgpt_response'}), name="get_chatgpt_response"),
    path('chatgpt/history', ChatGptViewSet.as_view({'get': 'get_history'}), name="get_history"),

]

