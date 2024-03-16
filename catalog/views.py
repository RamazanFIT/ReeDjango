from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Catalog
from .serializers import CatalogSerializer
from django.shortcuts import get_object_or_404




class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer
    
    # get
    def get_all_catalogs(self, request):
        queryset = Catalog.objects.all()
        serializer = CatalogSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)
    
    # get 
    def get_catalog(self, request, pk):
        catalog = Catalog.objects.filter(pk=pk)[0]
        serializer = CatalogSerializer(instance=catalog)
        return Response(data=serializer.data)
    
    # patch 
    def change_catalog(self, request):
        catalog = Catalog.objects.filter(pk=request.data['id'])[0]
        catalog.name = request.data['name']
        if (not request.data.get('file', True)) and catalog.file != request.data['file']:
            catalog.file = request.data['file']
        catalog.save()
        serializer = CatalogSerializer(instance=catalog)
        return Response(serializer.data)

    # delete 
    def delete_catalog(self, request, pk):
        catalog = Catalog.objects.filter(pk=pk)[0].delete()
        return Response({"detail" : "success"})
    
    def add_catalog(self, request):
        serializer = CatalogSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    

    
    

