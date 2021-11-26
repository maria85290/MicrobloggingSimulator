from django.shortcuts import render
import logging

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

logger = logging.getLogger(__name__)

@csrf_protect
def participate(request,*args, **kwargs):
        logger.warning('Participate Page was accessed at '+str(datetime.datetime.now())+' hours!')

        
        state, message, id = add_participant ()
        print(message)

        
        state, env = get_environment()

        logger.info("Ambiente de prototipação iniciado")

        state, config = get_configuration(env.configuration.configName)

        print(config.user_picture)
        ## vai buscar a base de dados n posts aleatorios.
        state, posts = get_posts(config.posts_number)
      

        return render (request, "tweet/participate.html", {"posts":posts, "idParticipant":id, "config":config})
      

def add_interaction (request, *args, **kwargs):
        
        ## Query recebida da interação, com Id do post, tipo de ação e id do participante
        query = request.GET.urlencode().split('-')
      
        id_post = query[0]
        action_type = query[1]
        participantId = query[2][:-1]

        print(id_post, action_type, participantId)
        state, env = get_environment()

        print(id_post, action_type, participantId, env.configuration)

        state, message = add_interactions({"postId": id_post, "participantId": participantId,"actionType": action_type, "configuration":env.configuration })

        logger.warning('['+str(datetime.datetime.now())+']' + message)
        
        print(message)

        return render (request, "tweet/participate.html")