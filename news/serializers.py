from rest_framework import serializers
from .models import News, AdditionalPhotosOfNews


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News 
        fields = ['id', 'title', 'main_photo', 'text', 'video']


class AdditionalPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalPhotosOfNews
        fields = ['id', 'fk', 'photo']
        


   