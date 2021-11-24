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

def get_posts (numberPosts):
    try:
        ## N posts aletorios
        post = Post.objects.all().order_by('?')[:numberPosts]
    except Post.DoesNotExist:
        return False, "Post does not exit"
    
    return True, post

def get_actionType_id (nameAction):
    try:
        action = Action_type.objects.get(name = nameAction)

    except Action_type.DoesNotExist:
        return False, "Action does not exit"

    return True, action.id


def add_participant ():
    
    try:
        x = Participant.objects.create(personality = 0, beginTime = datetime.datetime.now(), endTime =  '00:00:00' )
        id = x.id
    except Exception:
        error_message = "Error while creating new participant!"
        return False, error_message, 00


    state_message = "Partcipant was registered successfully!"
    return True, state_message, id


def add_interactions(data):
 
    postID = data.get('postId')
    action_type_id = get_actionType_id(data.get('actionType'))[1]
    participantID = data.get ('participantId') 

    print(postID)
    print(action_type_id)
    print(participantID)

    if data.get('actionType') == "reply":
        reply_content = data.get("reply_content") 
    
    try:
        Interaction.objects.create(actionType_id = action_type_id, replyContent = " ",post_id = postID, participant_id = participantID )
        state_message = "Objeto inserido com sucesso"
    
    except Exception:
        error_message = "Error while creating new interaction!"
        return False, error_message

    return True, state_message