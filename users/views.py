from rest_framework.response import Response
from rest_framework import viewsets, status
from users.models import *
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
import jwt, datetime
# checking auth token 



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
    serializer = UserSerializer(instance=user)
    
    return Response(data=serializer.data)

class AuthorizationViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer
    
    # post 
    def login(self, request):
        # [print(i) for i in range(100)]
        # print(request.GET)
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
    def test(self, request):
        response = checkAuthentication(request=request)
        # response.data['password'] = 'krutoi'
        return response

    # post 
    def logout(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {'status' : 'success'}
        return response

    