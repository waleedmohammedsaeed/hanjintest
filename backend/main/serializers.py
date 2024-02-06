from rest_framework import serializers
from .models import Branch, Category

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model= Branch
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'