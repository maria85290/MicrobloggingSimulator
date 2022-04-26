from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from django.core import serializers
from django.http import HttpResponse
import datetime
import json
import logging

from .models import *
from . import queries 
from . import random 

def writeLog (m):
        file_object = open('info.txt', 'a+')
        file_object.write(m)
        file_object.write('\n')
        file_object.close()
        return 0




'''
Render participate page and prepare the info
'''

@csrf_protect
def participate(request,*args, **kwargs):

      
        if request.session.get('env'):
                
              #  os.system('py mousetracking.py ' + str(request.session.get('id_user')) + "&")
                print(" [Session] An environment has already been generated for this session")

                
        else:     
                print("[Session] Generating a env for this session")
                state, env = queries.get_environment()
                state, config = queries.get_configuration(env.configuration.configName)     
                state, posts = queries.get_posts(config.posts_number)
                ## Check if the post have hashtags
                hashtags = []
                images = []
                for post in posts:
                  
                        state1, hashtag = queries.get_hashtags_by_post (post.id)
                        state2, img = queries.get_image_by_post(post.id)

                        if state1 == True:
                             hashtags.append ([k.hashtag for k in hashtag])
                             
                        if state2 == True:
                             images.append ([i.imagepath for i in img])
                             


                ## Save the data generated in the session
                request.session['env'] = env.id
                request.session['conf'] = model_to_dict(config)
                request.session['posts'] =  serializers.serialize('json',posts)
                request.session['hashtags'] = hashtags
                request.session['images'] = images
                request.session['submitedd'] = False
                 ## request.session['images'] =  ima

                request.session['interactions'] = {'like' : [], 'share': [], 'follow': [], "block":[], "retweet" :[], "comment":[]}

                       
                ## Data that is generated according to the settings 
                request.session['random_data'] = {
                        "interactions":  
                                random.interactions (request.session.get('conf')['posts_number'], request.session.get('conf')['lower_limit_interaction'], request.session.get('conf')['upper_limit_interaction'] ) ,
                        "names":  random.random_name (request.session.get('conf')['posts_number']),
                        "photo":  random.random_image(request.session.get('conf')['user_picture'], request.session.get('conf')['posts_number'])   }

         ## Check if the user has posts made by him to present
        state, posts_by_user = queries.get_posts_by_users (request.session.get('id_user'))

       # mousetracking.tracking(request.session.get('id_user'))

        if request.session.get('submitedd') == True:
                return render (request, "tweet/submitedd.html")
      


        context = {
         "posts":        zip (json.loads(request.session.get('posts')),request.session.get('hashtags'), request.session.get('images'), request.session.get('random_data')['interactions'],request.session.get('random_data')['names'], request.session.get('random_data')['photo']),
         "posts_by_user": posts_by_user, 
         "idParticipant": request.session.get('id_user'),
         "config":        request.session.get('conf'),
         'random_data':   request.session.get('random_data'),
         'interactions':  request.session.get('interactions')
        }
   

        return render (request, "tweet/participate.html", context)
      

'''
add a new interaction: like, block, follow, retwett, share. This function is called when the user clicks in one button
'''

@api_view(['GET', 'POST'])
def add_interaction (request, *args, **kwargs):
       
        
        ## Query recebida da interação, com Id do post, tipo de ação e id do participante
        query = request.GET.urlencode().split('-')
        id_post = query[0]
        print(id_post)
        action_type = query[1][:-1]
        ## print (action_type)
        
        state, env = queries.get_environment()


        context = {"post_id": id_post, 
        "participant_id": request.session.get('id_user'),
        "actionType_id": action_type,
        "configuration_id":env.configuration 
        }

        #Adiciona a base de dados

        state, message = queries.add_interactions(context)

        if   state   == True:
                writeLog('['+str(datetime.datetime.now())+']' + 'add_action:'+action_type+":"+str(id_post)+ ":" + str(request.session.get('id_user')))
                

        #edite random_data 
        positions =  [int(json.loads(request.session.get('posts'))[i]['pk']) for i in range (request.session.get('conf')['posts_number']) ]

        inte = request.session.get('random_data')['interactions']
        position =  positions.index(int(id_post))
        print ('ola', inte)
        position_action= ['comment','retweet', 'like', 'share', 'block', 'follow'].index(action_type)
        inte[position][position_action] = inte[position][position_action] + 1

        request.session['random_data'][0] = inte

        request.session['interactions'][action_type].append(int(id_post))
        request.session.modified = True

        print (request.session.get('random_data'))
        request.session.modified = True
        print ('ola', inte)

        
       ##  print (message)
        return render (request, "tweet/participate.html")


      

'''
add a new interaction: like, block, follow, retwett, share. This function is called when the user clicks in one button
'''

@api_view(['GET', 'POST'])
def remove_interaction (request, *args, **kwargs):
       
        print ("ola, cheguei ao remover")
        ## Query recebida da interação, com Id do post, tipo de ação e id do participante
        query = request.GET.urlencode().split('-')
        id_post = query[0]
        print(id_post)
        action_type = query[1][:-1]
        ## print (action_type)
        
        state, env = queries.get_environment()


        context = {"post_id": id_post, 
        "participant_id": request.session.get('id_user'),
        "actionType_id": action_type,
        "configuration_id":env.configuration 
        }

        #Adiciona a base de dados


        state, message = queries.delete_interaction(id_post, request.session.get('id_user'), action_type)

        if   state   == True:
                writeLog('['+str(datetime.datetime.now())+']' + 'delete_action:'+action_type+":"+str(id_post)+ ":" + str(request.session.get('id_user')))

        #edite random_data 
        positions =  [int(json.loads(request.session.get('posts'))[i]['pk']) for i in range (request.session.get('conf')['posts_number']) ]

        inte = request.session.get('random_data')['interactions']
        position =  positions.index(int(id_post))
        
        position_action= ['comment','retweet', 'like', 'share', 'block', 'follow'].index(action_type)
        inte[position][position_action] = inte[position][position_action] - 1

        request.session['random_data'][0] = inte

        print (request.session.get('random_data'))
        request.session.modified = True

        request.session['interactions'][action_type].remove(int(id_post))
        request.session.modified = True
      

        
       ##  print (message)
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
                       
                        post_id =  request.session.get('post_to_comment')
                        ## print ("post_id")
                        state, message = queries.add_interactions({"post_id": post_id, "participant_id": request.session.get('id_user'),"reply_content":content, "actionType_id": "reply", "configuration_id":env.configuration })
                        if state == True:
                                writeLog('['+str(datetime.datetime.now())+']' + 'add_reply'+":" + str(post_id) + ":" + str(request.session.get('id_user')) +  ":" + content.strip()  )

                        #edite random_data 
                        positions =  [int(json.loads(request.session.get('posts'))[i]['pk']) for i in range (request.session.get('conf')['posts_number']) ]

                        inte = request.session.get('random_data')['interactions']
                        position =  positions.index(int(post_id))
                        print ('ola', inte)
                        position_action= ['comment','retweet', 'like', 'share', 'block', 'follow'].index('comment')
                        inte[position][position_action] = inte[position][position_action] + 1

                        request.session['random_data'][0] = inte

                        request.session['interactions']['comment'].append(int(post_id))
                        request.session.modified = True

                        print (request.session.get('random_data'))
                        request.session.modified = True
                        print ('ola', inte)
                        
        return redirect (participate)
        

'''
add a post made by the user
'''
@api_view(['GET', 'POST'])
def add_post_by_user (request, *args, **kwargs):
        
        
        if request.method == 'POST':

                context =  {
                "post": request.data.get('post_by_user'), 
                "userID": request.session.get('id_user')
                }

                state, message = queries.add_post_by_user(context)
                if state == True:
                        writeLog ('['+str(datetime.datetime.now())+']' + 'add_post_by_user'+":" + str(request.session.get('id_user')) + ":" + request.data.get('post_by_user')  )
         
        return redirect (participate)

'''
Helper function: which allows  to add the post_id in the session to add a comment
'''
@api_view(['GET', 'POST'])
def update_session (request, *args, **kwargs):
        
        id_post = request.GET.urlencode()[:-1]
        
        request.session['post_to_comment'] = id_post
        return HttpResponse('ok')



'''
Helper function: which allows  to submit the participation
'''
@api_view(['POST'])
def submit (request, *args, **kwargs):
        if request.method == 'POST':
                state, message = queries.update_participant(request.session.get('id_user'))
                if state == True:
                        request.session['submitedd'] = True
        return redirect (participate)
      



