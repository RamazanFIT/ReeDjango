from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import ChatgptHistory
from .serializers import ChatgptHistorySerializer, ChatGptSerializer
from django.shortcuts import get_object_or_404
from users.models import User
# swagger 
from drf_yasg.utils import swagger_auto_schema

# permissions 
from users.views import isAdmin, isCustomer, isOwner, isAuthenticated, checkAuthentication

# chatgpt 
from chatgpt.chatgpt import generate_response


class ChatGptViewSet(viewsets.ModelViewSet):
    queryset = ChatgptHistory.objects.all()
    serializer_class = ChatgptHistorySerializer
    
    @swagger_auto_schema(operation_summary="chatgpt", request_body=ChatGptSerializer)
    def get_chatgpt_response(cls, request):
        if not isAuthenticated(request): return Response(data={"detail" : "Plz do Authentications"})
        serializer = ChatGptSerializer(data=request.data)
        if serializer.is_valid():
            chatgpt_message = generate_response(serializer.data.get("message"))
            
            # saving data 
            user = User.objects.get(pk=checkAuthentication(request).data.get('id'))
            data = ChatgptHistory(response_message=chatgpt_message, message=serializer.data.get("message"), user_id=user)
            data.save()
            
            return Response(data=chatgpt_message)
        else:
            return Response(data={"detail" : serializer.errors})
        
    @swagger_auto_schema(operation_summary="All history of messages with ChatGpt")
    def get_history(cls, request):
        if not isAuthenticated(request): return Response(data={"detail" : "Plz do Authentications"})
        try:
            messages = ChatgptHistory.objects.filter(user_id=checkAuthentication(request).data.get('id')).order_by('-created_at')
            serilaizer = ChatgptHistorySerializer(instance=messages, many=True)
            return Response(serilaizer.data)
        except:
            return Response(data={"detail" : "some error"}, status=status.HTTP_404_NOT_FOUND)
            


    