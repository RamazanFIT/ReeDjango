from rest_framework import serializers
from .models import News, AdditionalPhotosOfNews


class NewsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = News 
        fields = ['id', 'title', 'main_photo', 'text', 'video']


class AdditionalPhotosSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class Meta:
        model = AdditionalPhotosOfNews
        fields = ['id', 'fk', 'photo']
        


   