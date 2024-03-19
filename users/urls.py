from rest_framework import routers
from django.urls import include, path
from .views import AuthorizationViewSet

app_name = 'users'


urlpatterns = [
    # path('test/', TestViewSet.as_view({'get': 'get_list'}), name="someTest"),
    # path('test/<str:name>/', TestViewSet.as_view({'get': 'get_list'}), name="someTest"),
#     path('test/post', TestViewSet.as_view({'post': 'post_req'}), name="someTest"),

    path('login/', AuthorizationViewSet.as_view({'post': 'login'}), name="authorization"),
    path('signup/', AuthorizationViewSet.as_view({'post': 'signup'}), name="authorization"),
    path('get/', AuthorizationViewSet.as_view({'get': 'get_user'}), name="authorization"),
    path('logout/', AuthorizationViewSet.as_view({'post': 'logout'}), name="authorization"),
    
]

# r = routers.DefaultRouter()

# r.register(r'test', TestViewSet)

# urlpatterns += r.urls



# [print('1', end= " ") for i in range(100)]
# print(r.urls)
