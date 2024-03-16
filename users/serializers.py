from rest_framework import serializers


from .models import User 


# class SH(serializers.ModelSerializer):
#     class Meta:
#         model = SOMEMODEL
#         fields = '__all__'
        # fields = ['id', 'product', 'shop', 'price', 'quantity']



# class TestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Test 
#         fields = '__all__'
        
        

# class TestSerializer2(serializers.ModelSerializer):
#     class Meta:
#         model = Test2 
#         fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'password', 'email']