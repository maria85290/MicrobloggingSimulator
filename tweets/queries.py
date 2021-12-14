from types import CodeType
from .models import *
import datetime

'''
Ficheiro que contêm queries a consulta a base de dados
'''
 

###################################################
####  Queries de alteração da configuração do ambiente de estudo
###################################################

'''
Funçao que recebe o nome da configuração e devolve o objeto 
'''
def get_configuration (configName):
    try:
        conf = Configuration.objects.get(configName = configName)
    except Configuration.DoesNotExist:
        return False, "Config does not exit"
    
    return True, conf


'''
Funçao que devolve o ambiente
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
Funçao que devolve os posts com um dados id 
'''
def get_post (post_id):
    try:
        ## N posts aletorios
        post = Post.objects.filter(id = post_id)
    except Post.DoesNotExist:
        return False, "Post does not exit"
    return post


'''
Recebe um inteiro (numberPosts) e devolve esse número em posts
'''
def get_posts (numberPosts):
    try:
        ## N posts aletorios
        post = Post.objects.all().order_by('?')[:numberPosts]
    except Post.DoesNotExist:
        return False, "Post does not exit"

    return True, post



'''
Recebe o id de um utilizador e devolve os posts realizados por ele
'''
def get_posts_by_users (id_user):
    print("entrei na querie")

    try:
        ## N posts aletorios
        post = Post_by_participant.objects.filter(participant = get_participante (id_user))
    except Post_by_participant.DoesNotExist:
        return False, "User does not exit"
    
    return True, post


'''
Recebe o id de um utilizador e devolve o objeto 
'''
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


'''
Adiciona um novo participante a base de dados, sempre que o mesmo aceder
'''
def add_participant ():
    
    try:
        x = Participant.objects.create(personality = 0, beginTime = datetime.datetime.now(), endTime =  '00:00:00' )
        print(x.id)
    except Exception:
        error_message = "Error while creating new participant!"
        return False, error_message


    state_message = "Partcipant was registered successfully!"
    return x.id, state_message


'''
Adiciona uma nova interação a base de dados
'''
def add_interactions(data):
 
    postID = data.get('postId')
    action_type_id = get_actionType_id(data.get('actionType'))[1]
    participantID = data.get ('participantId') 
    configuration = data.get ('configuration') 

   # print(postID)
  #  print(action_type_id)
  #  print(participantID)
  #  print(configuration)


  #  print(part, post)

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



'''
Adiciona o conteudo postado por um dados utilizador a base de dados
'''
    
def add_post_by_user(data):
    print("entrou na query")

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