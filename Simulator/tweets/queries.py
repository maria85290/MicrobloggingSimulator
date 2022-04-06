from tkinter.tix import IMAGE
from types import CodeType
from .models import *
import datetime


###################################################
#### Study environment configuration change queries
###################################################

'''
Function that receives the name of the configuration and returns the object
'''
def get_configuration (configName):
    try:
        print (configName)
        conf = Configuration.objects.get(configName = configName)
    except Configuration.DoesNotExist:
        return False, "Config does not exit"
    
    return True, conf


'''
Function that returns the obj environment
'''
def get_environment ():
    try:
        env = Environment.objects.get()
    except Environment.DoesNotExist:
        return False, "Environment does not exit"
    
    return True, env




###################################################
####  Queries para consulta dos dados 
###################################################

'''
Function that returns the post with id = post_id
'''
def get_post (post_id):
    try:
        ## N posts aletorios
        post = Post.objects.filter(id = post_id)
    except Post.DoesNotExist:
        return False, "Post does not exit"
    return post


def get_actionType_id (nameAction):
    try:
        action = Action_type.objects.get(name = nameAction)

    except Action_type.DoesNotExist:
        return False, "Action does not exit"

    return True, action.id

'''
Receives an integer (numberPosts) and returns that number in posts
'''
def get_posts (numberPosts):
    try:
        ## N posts aletorios
        post = Post.objects.all().order_by('?')[:numberPosts]
    except Post.DoesNotExist:
        return False, "Post does not exit"

    return True, post



'''
Receives a user's id and returns the posts made by him
'''

def get_posts_by_users (id_user):
    #print("entrei na querie")

    try:
        ## N posts aletorios
        post = Post_by_participant.objects.filter(participant = get_participante (id_user))
    except Post_by_participant.DoesNotExist:
        return False, "User does not exit"
    
    return True, post

'''
Receives a post id and returns the hashtags associated
'''
def get_hashtags_by_post(id_post):
    try:
        hashtags = Hashtag.objects.filter(post_id = id_post)
    except Hashtag.DoesNotExist:
        return False, "Post does not exit"
    
    return True, hashtags



'''
Receives a post id and returns the images associated
'''
def get_image_by_post(id_post):
    try:
        images = Image.objects.filter(post_id = id_post)
    except IMAGE.DoesNotExist:
        return False, "Post does not exit"
    
    return True, images



'''
Receives a user's id and returns the corresponding object
'''
def get_participante (id_user):
    try:
        part = Participant.objects.get(id = id_user)
    except Participant.DoesNotExist:
        return False, "Participat does not exit"
    
    return part






'''
Add a new participant to the database
'''
def add_participant ():
    
    try:
        x = Participant.objects.create(personality = 0, beginTime = datetime.datetime.now(), endTime =  '00:00:00' )
    except Exception:
        error_message = "Error while creating new participant!"
        return False, error_message


    state_message = "Partcipant was registered successfully!"
    return x.id, state_message


'''
Add a new interaction to the database
'''
def add_interactions(data):
 
    postID = data.get('post_id')
    action_type_id = get_actionType_id(data.get('actionType_id'))[1]
    participantID = data.get ('participant_id') 
    configuration = data.get ('configuration_id') 


    
    try:
        interaction= Interaction.objects.create(actionType_id = action_type_id,  configuration_id = configuration.id,  participant_id = participantID, post_id = postID)
        state_message = "Interaction registered successfully!"
        if data.get ('reply_content'):
            action_reply.objects.create(interaction_id = interaction.id, content = data.get('reply_content'))
           
    except Exception:
        error_message = "Error while creating new interaction!"
        return False, error_message

    return True, state_message



'''
Adds the content posted by a user data to the database
'''
    
def add_post_by_user(data):
    #print("entrou na query")

    participantID = data.get ('userID') 
  #  configuration = data.get ('configuration') 
    post_content = data.get('post')

    #print(post_content, participantID)

    try:
        
        Post_by_participant.objects.create(participant_id = participantID, content = post_content)
        state_message = "Post by Participant registered successfully!"
    
    except Exception:
        error_message = "Error while creating new Post by Participant!"
        return False, error_message

    return True, state_message