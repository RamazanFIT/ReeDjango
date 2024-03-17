from django.shortcuts import render


from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Message
from .serializers import MessageSerializer
from django.shortcuts import get_object_or_404

# swagger 
from drf_yasg.utils import swagger_auto_schema



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    
    serializer_class = MessageSerializer
    
    def get_serializer_class(cls):
        # if self.request.method == 'POST' or self.request.method == 'PUT':
        #     return MessageSerializer
        return MessageSerializer
    
    # get 
    def get_all_message(cls, request):
        try:
            messages = Message.objects.all()
            serializator = MessageSerializer(instance=messages, many=True)
        except:
            return Response(data={"detail" : "not found"})
        return Response(data=serializator.data)
            
    # get 
    def get_message(cls, request, id):
        try:
            message = Message.objects.get(pk=id)
            serializator = MessageSerializer(instance=message)
        except:
            return Response(data={"detail" : "not found"})
        return Response(data=serializator.data)
    
    # delete 
    def delete_message(cls, request, id):
        try:
            Message.objects.get(pk=id).delete()
        except:
            return Response(data={"detail" : "not found"})
        return Response(data={"detail" : "success"})
    
    # post 
    def add_message(cls, request):
        try:
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
        try:
            message = Message.objects.get(pk=id)
            serializer = MessageSerializer(instance=message, data=request.data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(data={"detail" : serializer.errors})
        except:
            return Response(data={"detail" : "error"})
        return Response(data={"detail" : "success"})
    
    
        
    