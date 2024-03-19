from rest_framework.response import Response
from rest_framework import viewsets, status
from users.models import *
from users.serializers import UserSerializer, LoginSerializer, LogOutSerializer, AllUserDataSerializer
from django.shortcuts import get_object_or_404
import jwt, datetime


# swagger_setting_input_fields
# @swagger_auto_schema(operation_summary="info", request_body=Serializer)
from drf_yasg.utils import swagger_auto_schema




# class TestViewSet(viewsets.ModelViewSet):
#     queryset = Test.objects.all()
#     serializer_class = TestSerializer
    
#     list_ = [1, 2, 3, 4]
    
#     def get_list(self, request, name : str):
#         # return Response(data=self.list_, status=status.HTTP_200_OK)
#         return Response(data=name)
    
#     def post_req(self, request):
#         data = request.data['age']
#         return Response(data=data)


def checkAuthentication(request) -> Response:
    token = request.COOKIES.get('jwt')
        
    if not token:
        return Response(data={"permission" : "denied"})
    
    try:
        payload = jwt.decode(token, 'secret', algorithms='HS256')
    except jwt.ExpiredSignatureError:
        return Response(data={"permission" : "denied"})
    user_id = payload['id']
    
    user = User.objects.filter(pk=user_id)[0]
    serializer = AllUserDataSerializer(instance=user)
    
    return Response(data=serializer.data)

def isAdmin(request) -> bool:
    user = checkAuthentication(request)
    if user.data.get('type') == 'Admin':
        return True
    return False

def isCustomer(request) -> bool:
    user = checkAuthentication(request)
    if user.data.get('type') == 'Customer':
        return True
    return False

def isOwner(request) -> bool:
    user = checkAuthentication(request)
    if user.data.get('type') == 'Owner':
        return True
    return False

class AuthorizationViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    
    # post 
    @swagger_auto_schema(operation_summary="join to the system", request_body=LoginSerializer)
    def login(self, request):
        user = get_object_or_404(User, username=request.data["username"])
        if not user.check_password(request.data["password"]):
            return Response(data= {"detail" : "does not correct password"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(instance=user)
        
        payload = {
            'id' : user.id,
            'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'iat' : datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        
        response = Response()
        response.data={"token" : token, "user" : serializer.data}
        response.set_cookie(key='jwt', value=token, httponly=True)
        return response

    # post
    def signup(self, request):
        if request.data['user_type'] == 'Admin':
            return Response(data={"detail" : "permission denied"})
        
        serilalizer = UserSerializer(data=request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            user = User.objects.filter(username=request.data["username"])[0]
            
            user.set_password(request.data["password"])
            user.save()
            anotherSerializer = UserSerializer(instance=user)
            return Response({"token" : 1, "user" : anotherSerializer.data}, status=status.HTTP_200_OK)
        return Response(serilalizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # get 
    # def test(self, request):
    #     response = checkAuthentication(request=request)
    #     # response.data['password'] = 'krutoi'
    #     return response

    # post 
    @swagger_auto_schema(operation_summary="exit", request_body=LogOutSerializer)
    def logout(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'status' : 'success'}
        return response
    
    def get_user(cls, request):
        return checkAuthentication(request)


