from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Catalog, Reestr, PoiskPravoobladateley
from .serializers import CatalogSerializer, ReestrSerializer, PoiskPravoobladateleySerializer
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
    

class ReestrViewSet(viewsets.ModelViewSet):
    queryset = Reestr.objects.all()
    serializer_class = ReestrSerializer
    
    # get
    def get_all_reestrs(self, request):
        queryset = Reestr.objects.all()
        serializer = ReestrSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)
    
    # get 
    def get_reestr(self, request, pk):
        reestr = Reestr.objects.filter(pk=pk)[0]
        serializer = ReestrSerializer(instance=reestr)
        return Response(data=serializer.data)
    
    # patch 
    def change_reestr(self, request):
        reestr = Reestr.objects.filter(pk=request.data['id'])[0]
        reestr.name = request.data['name']
        if (not request.data.get('file', True)) and reestr.file != request.data['file']:
            reestr.file = request.data['file']
        reestr.save()
        serializer = ReestrSerializer(instance=reestr)
        return Response(serializer.data)

    # delete 
    def delete_reestr(self, request, pk):
        reestr = Reestr.objects.filter(pk=pk)[0].delete()
        return Response({"detail" : "success"})
    
    def add_reestr(self, request):
        serializer = ReestrSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    


class PoiskPravoobladateleyViewSet(viewsets.ModelViewSet):
    queryset = PoiskPravoobladateley.objects.all()
    serializer_class = ReestrSerializer
    
    # get
    def get_all_poisk_pravoobladateleys(self, request):
        queryset = PoiskPravoobladateley.objects.all()
        serializer = PoiskPravoobladateleySerializer(instance=queryset, many=True)
        return Response(data=serializer.data)
    
    # get 
    def get_poisk_pravoobladateley(self, request, pk):
        poisk_pravoobladateley = PoiskPravoobladateley.objects.filter(pk=pk)[0]
        serializer = PoiskPravoobladateleySerializer(instance=poisk_pravoobladateley)
        return Response(data=serializer.data)
    
    # patch 
    def change_poisk_pravoobladateley(self, request):
        poisk_pravoobladateley = PoiskPravoobladateley.objects.filter(pk=request.data['id'])[0]
        poisk_pravoobladateley.name = request.data['name']
        if (not request.data.get('file', True)) and poisk_pravoobladateley.file != request.data['file']:
            poisk_pravoobladateley.file = request.data['file']
        poisk_pravoobladateley.save()
        serializer = PoiskPravoobladateleySerializer(instance=poisk_pravoobladateley)
        return Response(serializer.data)

    # delete 
    def delete_poisk_pravoobladateley(self, request, pk):
        poisk_pravoobladateley = PoiskPravoobladateley.objects.filter(pk=pk)[0].delete()
        return Response({"detail" : "success"})
    
    def add_poisk_pravoobladateley(self, request):
        serializer = PoiskPravoobladateleySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
 