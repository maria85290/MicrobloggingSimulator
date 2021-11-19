from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_201_CREATED,
)

from .models import *
from .queries import *
from .serializers import *
# Create your views here.


'''
Render participate page
'''

def participate(request,*args, **kwargs):
        ## Numero de posts a mostar
        n = 2
        
        ## vai buscar a base de dados n posts aleatorios.
        state, posts = get_posts(n)
      

        return render (request, "tweet/participate.html", {"posts":posts})
      

def add_interaction (request, *args, **kwargs):
        return 0