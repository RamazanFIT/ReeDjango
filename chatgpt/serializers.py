from rest_framework import serializers
from .models import ChatgptHistory


class ChatgptHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatgptHistory 
        fields = ['message', 'response_message']
    
class ChatGptSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=2000)
      


   