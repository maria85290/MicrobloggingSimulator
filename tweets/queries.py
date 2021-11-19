from types import CodeType
from .models import *


def get_posts (numberPosts):
    try:
        post = Post.objects.all().order_by('?')[:numberPosts]
    except Post.DoesNotExist:
        return False, "Post does not exit"
    
    return True, post

def get_actionType (nameAction):
    try:
        action = Action_type.objects.get(name = nameAction)

    except Action_type.DoesNotExist:
        return False, "Action does not exit"

    return True, action


def add_participant (data):
    
    try:
        Participant.objects.create()
    
    except Exception:
        error_message = "Error while creating new participant!"
        return False, error_message


    state_message = "Partcipant was registered successfully!"
    return True, state_message


def add_interaction(data):
    postID = data.get('postId')
    action_type_id = get_actionType(data.get('actionType'))
    participantID = data.get ('participantId') 

    if data.get('actionType') == "reply":
        reply_content = data.get("reply_content") 
    
    try:
        Interaction.objects.create(actionTypeID =action_type_id, post = postID, participant = participantID )
    
    except Exception:
        error_message = "Error while creating new interaction!"
        return False, error_message