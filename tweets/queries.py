from types import CodeType
from .models import *
import datetime
 

###################################################
####  Queries de alteração da configuração do ambiente de estudo
###################################################


def get_configuration (configName):
    try:
        conf = Configuration.objects.get(configName = configName)
    except Configuration.DoesNotExist:
        return False, "Config does not exit"
    
    return True, conf



def get_environment ():
    try:
        env = Environment.objects.get()
    except Environment.DoesNotExist:
        return False, "Environment does not exit"
    
    return True, env




###################################################
####  Queries para consulta dos dados 
###################################################

def get_post (post_id):
    try:
        ## N posts aletorios
        post = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        return False, "Post does not exit"
    return post


def get_posts (numberPosts):
    try:
        ## N posts aletorios
        post = Post.objects.all().order_by('?')[:numberPosts]
    except Post.DoesNotExist:
        return False, "Post does not exit"

    return True, post
    
def get_posts_by_users (id_user):
    print("entrei na querie")

    try:
        ## N posts aletorios
        post = Post_by_participant.objects.filter(participant = get_participante (id_user))
    except Post_by_participant.DoesNotExist:
        return False, "User does not exit"
    
    return True, post

def get_participante (id_user):
    try:
        part = Participant.objects.get(id = id_user)
    except Participant.DoesNotExist:
        return False, "Participat does not exit"
    
    return part

def get_actionType_id (nameAction):
    try:
        action = Action_type.objects.get(name = nameAction)

    except Action_type.DoesNotExist:
        return False, "Action does not exit"

    return True, action.id


def add_participant ():
    
    try:
        x = Participant.objects.create(personality = 0, beginTime = datetime.datetime.now(), endTime =  '00:00:00' )
        print(x.id)
    except Exception:
        error_message = "Error while creating new participant!"
        return False, error_message


    state_message = "Partcipant was registered successfully!"
    return x.id, state_message


def add_interactions(data):
 
    postID = data.get('postId')
    action_type_id = get_actionType_id(data.get('actionType'))[1]
    participantID = data.get ('participantId') 
    configuration = data.get ('configuration') 

    print(postID)
    print(action_type_id)
    print(participantID)
    print(configuration)

    part = get_participante (participantID)
    post = get_post(postID)

    print(part, post)

    reply_content = " "

    if data.get('actionType') == "reply":
        reply_content = data.get("reply_content") 
    
    try:
        Interaction.objects.create(actionType_id = action_type_id, replyContent = reply_content,post_id = postID, participant_id = participantID,  configuration = configuration)
        state_message = "Interaction registered successfully!"
    
    except Exception:
        error_message = "Error while creating new interaction!"
        return False, error_message

    return True, state_message


    
def add_post_by_user(data):
    print("entrou na query")

    participantID = data.get ('userID') 
  #  configuration = data.get ('configuration') 
    post_content = data.get('post')

    print(post_content, participantID)

    try:
        Post_by_participant.objects.create(participant_id = participantID, content = post_content)
        state_message = "Post by Participant registered successfully!"
    
    except Exception:
        error_message = "Error while creating new Post by Participant!"
        return False, error_message

    return True, state_message