from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Document
from .serializers import DocumentSerializer
from django.shortcuts import get_object_or_404

# permissions 
from users.views import isAdmin, isCustomer, isOwner, isAuthenticated, checkAuthentication


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    
    # get
    def get_all_documents(self, request):
        queryset = Document.objects.all()
        serializer = DocumentSerializer(instance=queryset, many=True)
        return Response(data=serializer.data)
    
    # get 
    def get_document(self, request, pk):
        document = Document.objects.filter(pk=pk)[0]
        serializer = DocumentSerializer(instance=document)
        return Response(data=serializer.data)
    
    # patch 
    def change_document(self, request):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                        data={"detail" : "permission denied"})
        document = Document.objects.filter(pk=request.data['id'])[0]
        document.label = request.data['label']
        if (not request.data.get('file', True)) and document.file != request.data['file']:
            document.file = request.data['file']
        document.save()
        serializer = DocumentSerializer(instance=document)
        return Response(serializer.data)

    # delete 
    def delete_document(self, request, pk):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                        data={"detail" : "permission denied"})

        document = Document.objects.filter(pk=pk)[0].delete()
        return Response({"detail" : "success"})
    
    def add_document(self, request):
        if not isAdmin(request): 
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE, 
                        data={"detail" : "permission denied"})
        serializer = DocumentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
