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
import random


'''
Render participate page
'''

participantId = 00

@csrf_protect
def participate(request,*args, **kwargs):
        

        state, message, id = add_participant ()
        print(message)


        state, env = get_environment()

        state, config = get_configuration(env.configuration.configName)

        print(config.user_picture)
        ## vai buscar a base de dados n posts aleatorios.
        state, posts = get_posts(config.posts_number)
      

        return render (request, "tweet/participate.html", {"posts":posts, "idParticipant":id, "config":config})
      

def add_interaction (request, *args, **kwargs):
        
        ## Querie recebida da interação, com Id do post, tipo de ação e id do participante
        query = request.GET.urlencode().split('-')
      
        id_post = query[0]
        action_type = query[1]
        participantId = query[2][:-1]

        print(id_post, action_type, participantId)
        
        state, message = add_interactions({"postId": id_post, "participantId": participantId,"actionType": action_type })

        print(message)

        return render (request, "tweet/participate.html")