from django.shortcuts import redirect, render
import logging

from .models import *
from . import queries 
from .serializers import *
from django.core import serializers
# Create your views here.
from django.http import HttpResponse

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_protect
import random
import datetime
from django.forms.models import model_to_dict

import json

'''
Render participate page
'''

participantId = 00

logger = logging.getLogger(__name__)

@csrf_protect
def participate(request,*args, **kwargs):

        logger.warning ('['+str(datetime.datetime.now())+']' + 'userId:' + str(request.session.get('id_user')))

        if request.session.get('env'):
                print(" [Session] An environment has already been generated for this session")
     
        else:     
                print(" [Session] Generating a env for this session")
                state, env = queries.get_environment()
                state, config = queries.get_configuration(env.configuration.configName)
                ## vai buscar a base de dados n posts aleatorios.      
                state, posts = queries.get_posts(config.posts_number)

                ## Guarda os dados gerados na sessao
                request.session['env'] = env.id
                request.session['conf'] = model_to_dict(config)
                request.session['posts'] =  serializers.serialize('json',posts)  

        state, posts_by_user = queries.get_posts_by_users (request.session.get('id_user'))
      #  print (posts_by_user)

        ## Verificar se o user tem posts realizados por ele para apresentar
        state, posts_by_user = queries.get_posts_by_users(request.session.get('id_user'))

        context = {
          "posts":json.loads(request.session.get('posts')),
         "posts_by_user" : posts_by_user, 
         "idParticipant":request.session.get('id_user'),
         "config":request.session.get('conf')
        }
        
        return render (request, "tweet/participate.html", context)
      
@api_view(['GET', 'POST'])
def add_interaction (request, *args, **kwargs):
        
        ## Query recebida da interação, com Id do post, tipo de ação e id do participante
        query = request.GET.urlencode().split('-')
        id_post = query[0]
        action_type = query[1][:-1]
        
        state, env = queries.get_environment()

        logger.warning ('['+str(datetime.datetime.now())+']' + 'add_action:'+action_type+":"+str(id_post)+ ":" + str(request.session.get('id_user')))

        context = {"postId": id_post, 
        "participantId": request.session.get('id_user'),
        "actionType": action_type, 
        "configuration":env.configuration 
        }

        state, message = queries.add_interactions(context)

        
        return render (request, "tweet/participate.html")


@api_view(['GET', 'POST'])
def add_reply (request, *args, **kwargs):
         ## Query recebida com o comentario
        ##query = request.GET.urlencode()
        
       ## content = query[:-1]

        if request.method == 'POST':

                content=  request.data.get('comment')
                
                state, env = queries.get_environment()

                if request.session.get('post_to_comment'):
                        post_id =  request.session.get('post_to_comment')
                        state, message = queries.add_interactions({"postId": post_id, "participantId": request.session.get('id_user'),"reply_content":content, "actionType": "reply", "configuration":env.configuration })
                        if state == True:
                                logger.warning ('['+str(datetime.datetime.now())+']' + 'add_reply'+":" + str(request.session.get('id_user')) + ":" + str(post_id) + ":" + content  )
         
        
        return redirect (participate)
        

@api_view(['GET', 'POST'])
def add_post_by_user (request, *args, **kwargs):
        
        
        if request.method == 'POST':
                print("estrou no post") 

                context =  {
                "post": request.data.get('post_by_user'), 
                "userID": request.session.get('id_user')
                }

                state, message = queries.add_post_by_user(context)
                if state == True:
                        logger.warning ('['+str(datetime.datetime.now())+']' + 'add_post_by_user'+":" + str(request.session.get('id_user')) + ":" + request.data.get('post_by_user')  )
         
        return redirect (participate)

'''
Função que permite adicionar a seção o id do post a adicionar comentario 
'''
@api_view(['GET', 'POST'])
def update_session (request, *args, **kwargs):
        
        id_post = request.GET.urlencode()[:-1]
        
        request.session['post_to_comment'] = id_post
        return HttpResponse('ok')

        