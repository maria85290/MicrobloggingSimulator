import random
from django import template
import os
register = template.Library()


##################################
#### Gerar um número inteiro num interbalo [a,b]
###################################
@register.simple_tag
def random_int(a, b):
    return random.randint(a, b)


@register.simple_tag
def random_name():
    list_name = ["Maria Laura", "Filipa silva" , "João Pedro","Middleton Mays","Teri Crosby", "Constança Elias" ,"Barron Knox" , "Rowland Banks" , "Ryan Branch"]
    return random.choice(list_name)



@register.simple_tag
def random_image(userPic):
    if userPic == False:
        picList = os.listdir(os.getcwd() +"/static/users/images") 
        pic ="images/" +  random.choice(picList)
    else:
        picList = os.listdir(os.getcwd() +"/static/users/pictures") 
        pic = "pictures/" + random.choice(picList)

    return 'static/users/' + pic





