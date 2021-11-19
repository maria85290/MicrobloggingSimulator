from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post 
        fields = ('content', 'image')
  #  content = serializers.CharField(required=True)
  #  image = serializers.CharField()
   

 