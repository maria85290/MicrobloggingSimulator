from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from django.core import serializers
from django.http import HttpResponse
import logging
import datetime
import json


from .models import *
from . import queries 
from . import random 


logger = logging.getLogger(__name__)


'''
Render participate page and prepare the info
'''

@csrf_protect
def participate(request,*args, **kwargs):

      
        if request.session.get('env'):
                print(" [Session] An environment has already been generated for this session")
     
        else:     
                print(" [Session] Generating a env for this session")
                state, env = queries.get_environment()
                state, config = queries.get_configuration(env.configuration.configName)     
                state, posts = queries.get_posts(config.posts_number)


                ## Save the data generated in the session
                request.session['env'] = env.id
                request.session['conf'] = model_to_dict(config)
                request.session['posts'] =  serializers.serialize('json',posts)

                ## Data that is generated according to the settings 
                request.session['random_data'] = {
                        "interactions":  
                                random.interactions (request.session.get('conf')['posts_number'], request.session.get('conf')['lower_limit_interaction'], request.session.get('conf')['upper_limit_interaction'] ) ,
                        "names":  random.random_name (request.session.get('conf')['posts_number']),
                        "photo":  random.random_image(request.session.get('conf')['user_picture'], request.session.get('conf')['posts_number'])   }

         ## Check if the user has posts made by him to present
        state, posts_by_user = queries.get_posts_by_users (request.session.get('id_user'))

        context = {
          "posts": zip (json.loads(request.session.get('posts')),request.session.get('random_data')['interactions'],request.session.get('random_data')['names'], request.session.get('random_data')['photo']),
          "posts_by_user" : posts_by_user, 
         "idParticipant":request.session.get('id_user'),
         "config":request.session.get('conf'),
         'random_data':  (request.session.get('random_data'))
        }
       # logger.warning ('['+str(datetime.datetime.now())+']' + 'userId:' + str(request.session.get('id_user')))


        return render (request, "tweet/participate.html", context)
      

'''
add a new interaction: like, block, follow, retwett, share. This function is called when the user clicks in one button
'''

@api_view(['GET', 'POST'])
def add_interaction (request, *args, **kwargs):
       
        
        ## Query recebida da interação, com Id do post, tipo de ação e id do participante
        query = request.GET.urlencode().split('-')
        id_post = query[0]
        action_type = query[1][:-1]
        print (action_type)
        
        state, env = queries.get_environment()


        context = {"post_id": id_post, 
        "participant_id": request.session.get('id_user'),
        "actionType_id": action_type,
        "configuration_id":env.configuration 
        }

        state, message = queries.add_interactions(context)

        if   state   == True:
                logger.warning ('['+str(datetime.datetime.now())+']' + 'add_action:'+action_type+":"+str(id_post)+ ":" + str(request.session.get('id_user')))


        print (message)
        return render (request, "tweet/participate.html")


'''
add a new interaction: reply. This function is called when the user clicks in one button
'''
@api_view(['GET', 'POST'])
def add_reply (request, *args, **kwargs):
         ## Query recebida com o comentario
        ##query = request.GET.urlencode()
        
       ## content = query[:-1]
      
        if request.method == 'POST':

                content=  request.data.get('comment')
                
                state, env = queries.get_environment()

                if request.session.get('post_to_comment'):
                        print ("ola")
                        post_id =  request.session.get('post_to_comment')
                        print ("post_id")
                        state, message = queries.add_interactions({"post_id": post_id, "participant_id": request.session.get('id_user'),"reply_content":content, "actionType_id": "reply", "configuration_id":env.configuration })
                        if state == True:
                                logger.warning ('['+str(datetime.datetime.now())+']' + 'add_reply'+":" + str(post_id) + ":" + str(request.session.get('id_user')) +  ":" + content.strip()  )
         
        
        return redirect (participate)
        

'''
add a post made by the user
'''
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
Helper function: which allows  to add the post_id in the session to add a comment
'''
@api_view(['GET', 'POST'])
def update_session (request, *args, **kwargs):
        
        id_post = request.GET.urlencode()[:-1]
        
        request.session['post_to_comment'] = id_post
        return HttpResponse('ok')

        