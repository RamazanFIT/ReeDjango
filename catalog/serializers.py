from rest_framework import serializers
from .models import Catalog, Reestr, PoiskPravoobladateley, InostrannyeOkupy

        
class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog 
        fields = ['id', 'name', 'file']

     
     
          
class ReestrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reestr 
        fields = ['id', 'name', 'file']

class PoiskPravoobladateleySerializer(serializers.ModelSerializer):
    class Meta:
        model = PoiskPravoobladateley 
        fields = ['id', 'name', 'file']
        

class InostrannyeOkupySerializer(serializers.ModelSerializer):
    class Meta:
        model =  InostrannyeOkupy
        fields = ['id', 'text', 'title']
        