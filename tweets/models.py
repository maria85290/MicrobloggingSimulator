from django.db import models



# Create your models here.


#################################
## Este modelo é responsavel pela configuração do estudo 
##################################


class Configuration (models.Model):
    configName = models.CharField(max_length=10) 
    space_for_comment = models.BooleanField(default = 0) ## caixa de textxo para escrever comentário
    space_for_creat_post = models.BooleanField(default = 0) 
    user_picture  =  models.BooleanField(default = 0)   # O criador do post tem foto de perfil
    reply_button =  models.BooleanField(default = 0)  
    like_button =  models.BooleanField(default = 0)  
    share_button =  models.BooleanField(default = 0)  
    block_button =  models.BooleanField(default = 0)  
    follow_button =  models.BooleanField(default = 0)  
    retweet_button =  models.BooleanField(default = 0)  
    posts_number = models.IntegerField(default = 1)
    lower_limit_interaction = models.IntegerField(default=1)    #limite inferior de numero de interações
    upper_limit_interaction = models.IntegerField(default=1)     # limite superior número de interações

class Environment (models.Model):
    configuration =  models.ForeignKey(Configuration, on_delete=models.CASCADE)

#####################################################
### Modelos de dados
###################################################

class Participant(models.Model):
    personality = models.IntegerField(default=0)
    beginTime = models.TimeField()
    endTime = models.TimeField()


class Mouse_tracking (models.Model):
    tracking = models.CharField(max_length=100) 
    participant =  models.ForeignKey(Participant, on_delete=models.CASCADE)


class Post_by_participant (models.Model):
    participant =  models.ForeignKey(Participant, on_delete=models.CASCADE)
    content  = models.CharField(max_length=280) 


class Post (models.Model):
    content  = models.CharField(max_length=280) 
    image = models.CharField(max_length=50, null=True)

class Hashtag(models.Model):
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    hashtag = models.CharField(max_length=30) 
    
class Action_type(models.Model):
    name = models.CharField(max_length=30) 

class Interaction (models.Model):
    actionType = models.ForeignKey(Action_type, on_delete=models.CASCADE)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    participant =  models.ForeignKey(Participant, on_delete=models.CASCADE)
    replyContent = models.CharField(max_length=280, default=" ") 
    configuration = models.ForeignKey(Configuration, on_delete=models.CASCADE)

