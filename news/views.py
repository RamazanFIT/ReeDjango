from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import News, AdditionalPhotosOfNews
from .serializers import NewsSerializer, AdditionalPhotosSerializer
from django.shortcuts import get_object_or_404

# swagger 
from drf_yasg.utils import swagger_auto_schema



class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    
    serializer_class = NewsSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return AdditionalPhotosSerializer
        return NewsSerializer

    # get 
    @swagger_auto_schema(operation_summary="getting all of the news form site")
    def get_all_news(self, request):
        queryset = News.objects.all()
        serializer = NewsSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)
    
    # get 
    def get_new(self, request, id : int):
        new = News.objects.get(pk=id)
        serializer = NewsSerializer(instance=new)
        return Response(data=serializer.data)
    
    # get 
    def get_new_additional_images(self, request, id : int):
        photos = AdditionalPhotosOfNews.objects.filter(fk=id)
        serializer = AdditionalPhotosSerializer(instance=photos, many=True)
        return Response(data=serializer.data)

    # post
    # @swagger_auto_schema(operation_summary="getting all of the news form site", request_body=AdditionalPhotosSerializer)
    def create_new(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"detail" : serializer.errors})
        return Response(data=serializer.data)
    
    # delete 
    def delete_new(self, request, id : int):
        try:
            document = News.objects.filter(pk=id)[0].delete()
        except:
            return Response({"detail" : "Not Found"})
        return Response({"detail" : "success"})
    

    
    # post 
    @swagger_auto_schema(request_body=AdditionalPhotosSerializer)
    def add_additional_photo(self, request):
        serializer = AdditionalPhotosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"detail" : serializer.errors})
        return Response(data=serializer.data)
    
    # delete 
    def delete_additional_photo(self, request, id):
        try:
            additional_photo = AdditionalPhotosOfNews.objects.get(pk=id)
            additional_photo.delete()
        except:
            return Response({"detail" : "Not Found"})
        return Response({"detail" : "success"})
    
    # put 
    def change_new(self, request):
        
        try:
            news_instance = News.objects.get(pk=request.data['id'])
        except News.DoesNotExist:
            return Response({'message': 'News not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = NewsSerializer(data=request.data, instance=news_instance)
        
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(data={"detail": serializer.errors})
        return Response(data={"detail" : "success"})
    
    # put 
    @swagger_auto_schema(request_body=AdditionalPhotosSerializer)
    def change_additional_photo(sefl, request):
        
        try:
            news_instance = AdditionalPhotosOfNews.objects.get(pk=request.data['id'])
        except News.DoesNotExist:
            return Response({'message': 'News photo not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = AdditionalPhotosSerializer(data=request.data, instance=news_instance)
        
        if serializer.is_valid():
            serializer.save()
        else:
            return Response(data={"detail": serializer.errors})
        return Response(data={"detail" : "success"})

    
