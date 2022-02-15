import random
from django import template
import os
register = template.Library()


##################################
#### Generate a list with n integers in a range [a,b]
###################################
def random_list_int(a, b, n):
    return [random.randint(a, b)  for i in range (n)]





#### Generate a list with n lists of integers

def interactions (posts_number, min, max ):
    l =  [random_list_int(min, max, 6)  for i in range (posts_number)]
    return l


#### Sellect n elements from list
def random_name(n):
    list_name = ["Maria Laura", "Filipa silva" , "João Pedro","Middleton Mays","Teri Crosby", "Constança Elias" ,"Barron Knox" , "Rowland Banks" , "Ryan Branch"]
    return random.sample(list_name,n )




def random_image(userPic, n):
    l = []
    for i in range(n):
       
        if userPic == False:
            picList = os.listdir(os.getcwd() +"/static/users/images") 
            pic ="static/users/images/" +  random.choice(picList)
        else:
            picList = os.listdir(os.getcwd() +"/static/users/pictures") 
            pic = "static/users/pictures/" + random.choice(picList)
        l.append (pic)

    return l





