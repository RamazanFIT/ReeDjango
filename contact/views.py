from django.shortcuts import render


from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Message
from .serializers import MessageSerializer
from django.shortcuts import get_object_or_404

# swagger 
from drf_yasg.utils import swagger_auto_schema

# permissions 
from users.views import isAdmin, isCustomer, isOwner, isAuthenticated, checkAuthentication


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    
    serializer_class = MessageSerializer
    
    def get_serializer_class(cls):
        # if self.request.method == 'POST' or self.request.method == 'PUT':
        #     return MessageSerializer
        return MessageSerializer
    
    # get 
    def get_all_message(cls, request):
        if not isAdmin(request) : return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            messages = Message.objects.all()
            serializator = MessageSerializer(instance=messages, many=True)
        except:
            return Response(data={"detail" : "not found"})
        return Response(data=serializator.data)
            
    # get 
    def get_own_message(cls, request):
        if not isAuthenticated(request): return Response(data={"detail" : "not found"})
        try:
            # message = Message.objects.get(pk=id)
            # serializator = MessageSerializer(instance=message)
            user = checkAuthentication(request)
            messages = Message.objects.filter(sender=user.data['id'])
            serializator = MessageSerializer(instance=messages, many=True)
            return Response(data=serializator.data)
        except:
            return Response(data={"detail" : "not found"})
    
    def get_received_message(cls, request):
        if not isAuthenticated(request): return Response(data={"detail" : "not found"})
        try:
            user = checkAuthentication(request)
            messages = Message.objects.filter(receiver=user.data['id'])
            serializator = MessageSerializer(instance=messages, many=True)
            return Response(data=serializator.data)
        except:
            return Response(data={"detail" : "not found"})

    # delete 
    def delete_message(cls, request, id):
        if not isAuthenticated(request): return Response(data={"detail" : "not found"})
        try:
            message = Message.objects.get(pk=id)
            if message.sender.id != checkAuthentication(request).data['id']: return Response(data={"detail" : "permission denied"})
            message.delete()
            return Response(data={"detail" : "success"})
        except:
            return Response(data={"detail" : "not found"})
        return Response(data={"detail" : "success"})
    
    # post 
    def add_message(cls, request):
        if not isAuthenticated(request): return Response(data={"detail" : "not found"})
        try:
            request.data['sender'] = checkAuthentication(request).data['id']
            serializer = MessageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(data={"detail" : serializer.errors})
        except:
            return Response(data={"detail" : "error"})
        return Response(data={"detail" : "success"})

    # put 
    def change_message(cls, request, id : int):
        if not isAuthenticated(request): return Response(data={"detail" : "not found"})
        try:
            message = Message.objects.get(pk=id)
            if message.sender.id != checkAuthentication(request).data['id']: 
                return Response(data={"detail" : "permission denied"})
            
            serializer = MessageSerializer(instance=message, data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(data={"detail" : serializer.errors})
        except:
            return Response(data={"detail" : "error"})
        return Response(data={"detail" : "success"})
    
    
        
    