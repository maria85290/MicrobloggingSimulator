import datetime
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,  EmailMessage


logger = logging.getLogger(__name__)




'''
Render Home page 
'''
def home_view(request,*args, **kwargs):  
    return render (request, "home.html", {})



'''
Render about page
'''
def about_view(request,*args, **kwargs):
    return render (request, "about.html")




'''
Render contact form and send e-mail
'''
def contact_view(request,*args, **kwargs):
   
    if request.session.test_cookie_worked():
                print ("The test cookie worked!!!")
                request.session.delete_test_cookie()

    if request.method =="POST":
        Name   = request.POST['Name']
        Email  = request.POST['Email']
        Subject = request.POST['Subject']
        Message = request.POST['Message']
        print(Name, Email, Subject, Message)

        ## Send the e-mail
        send_mail (
           '[Prototyping Environment]' + Subject , #subject
            "[send by] " + Email + "\n" + Message, #message
            Email, #from Email
            ['mei.proj2122@gmail.com'], #TO Email
        )


        return render (request, "contact.html", {"name": Name})

    else:
        return render (request, "contact.html", {})