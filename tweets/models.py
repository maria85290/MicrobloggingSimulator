from django.db import models

# Create your models here.
## Outros campos que podem aqui ser identificados:
## follows_list, time etz

class Participant(models.Model):
    personality = models.IntegerField(blank=True)
    durationParticipation = models.TimeField(blank=True)


class Mouse_tracking (models.Model):
    tracking = models.CharField(max_length=100) 
    participant =  models.ForeignKey(Participant, on_delete=models.CASCADE)


class Post (models.Model):
    content  = models.CharField(max_length=280) 
    image = models.CharField(max_length=50, blank=True)

class Hashtag(models.Model):
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    hashtag = models.CharField(max_length=30, blank=True) 
    
class Action_type(models.Model):
    name = models.CharField(max_length=30) 

class Interaction (models.Model):
    actionType = models.ForeignKey(Action_type, on_delete=models.CASCADE)
    post =  models.ForeignKey(Post, on_delete=models.CASCADE)
    participant =  models.ForeignKey(Participant, on_delete=models.CASCADE)
    replyContent = models.CharField(max_length=280, blank=True) 
