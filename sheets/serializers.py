from rest_framework import serializers
from .models  import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product
        fields = "__all__"
        from rest_framework import serializers
from .models import Customer, Harid

class HaridSerializer(serializers.ModelSerializer):
    class Meta:
        model = Harid
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    haridlar = HaridSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
