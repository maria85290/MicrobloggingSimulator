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

from django.views.decorators.csrf import csrf_protect

'''
Render participate page
'''
@csrf_protect
def participate(request,*args, **kwargs):

        state, message = add_participant ()

        print(message)
        ## Numero de posts a mostar
        n = 2
        
        ## vai buscar a base de dados n posts aleatorios.
        state, posts = get_posts(n)
      

        return render (request, "tweet/participate.html", {"posts":posts})
      

def add_interaction (request, *args, **kwargs):
        ## Querie recebida da interação
        query = request.GET.urlencode().split('-')
      
        id_post = query[0]

        action_type = query[1][:-1]

        print(id_post, action_type)
        
        state, message = add_interactions({"postId": id_post, "participantId": 3,"actionType": action_type })

        print(message)

        return render (request, "tweet/participate.html")