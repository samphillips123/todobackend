from .models import Todo
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# out TodoSerializer
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # model it will serialize
        model = Todo
        # fields that should be included
        fields = ['id', 'subject', 'details']
        
