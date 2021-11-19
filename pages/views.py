from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail,  EmailMessage

'''
Render Home page 
'''
def home_view(request,*args, **kwargs):
    print(request.user)
    return render (request, "home.html", {})



'''
Render about page
'''
def about_view(request,*args, **kwargs):
    my_context = {
     #   "about" : ["Esta plataforma integra um projeto acadêmico, a decorrer na Universidade do Minho - Portugal, cujo propósito é obter um algoritmo capaz de gerar Posts (mensagens que se publicam numa página de internet) despertando Sentimentos e interagindo com a Personalidade dos utilizadores.", "O uso de redes sociais e da comunicação online têm vindo a crescer exponencialmente ao longo dos últimos anos. Em 2021, 56.8 % da população mundial possui um perfil em pelo menos uma rede. Consequentemente, a difusão de fake news teve um crescimento proporcional. Surgiu assim, a necessidade de validar a informação que surge online, o que promoveu o surgimento de agências que se dedicam exclusivamente a esta tarefa. Porém, um post fazer referência a uma entidade credível de validação de fatos não garante a sua leitura. É necessário mais. A realidade é que a maioria das vezes este tipo de publicação passa ao lado e a informação nele contida, por vezes valiosa, escapa ao utilizador. É fundamental contrariar esta tendência. Neste projeto, recorrer-se-á a introdução de sentimentos nos Posts e a análise da personalidade dos leitores, com o objetivo de despertar interesse, promover interação e uma maior aceitação do conteúdo divulgado.", "Esta plataforma, pretende ser o ponto de partida para este estudo, permitindo recolher e colecionar dados, possibilitando a identificação de tendências no que diz respeito às decisões dos utilizadores de uma rede social quando confrontados com uma dada publicação."]
     "about" : ["This platform is part of an academic project, taking place at the University of Minho - Portugal, whose purpose is to obtain an algorithm capable of generating Posts (messages that are published on a website) awakening Feelings and interacting with the Personality of users. "," The use of social networking and online communication has been growing exponentially over the past few years. In 2021, 56.8% of the world's population has a profile in at least one social media. Consequently, the spread of fake news had a proportional growth. Thus, there was a need to validate information that appears online, which promoted the emergence of agencies that are dedicated exclusively to this task. However, a post referring to a credible fact-validation entity does not guarantee its reading. More is needed. The reality is that most of the time this type of publication is overlooked and the information it contains, sometimes valuable, escapes the user. It is essential to change this trend. In this project, it will be used the introduction of feelings in the Posts and the analysis of the readers personality, in order to arouse interest, promote interaction and a greater acceptance of the published content. "," This platform, is intended to be the starting point for this study, allowing to collect data, enabling the identification of trends regarding the decisions of users of a social media when confronted with a given publication. "]
    }
    return render (request, "about.html", my_context)




'''
Render contact form and send e-mail
'''
def contact_view(request,*args, **kwargs):
    if request.method =="POST":
        Name   = request.POST['Name']
        Email  = request.POST['Email']
        Subject = request.POST['Subject']
        Message = request.POST['Message']
        print(Name, Email, Subject, Message)

        Email = 'mei.proj2122@gmail.com'
        ## Send the e-mail
        send_mail (
           '[Prototyping Environment]' + Subject , #subject
             Message, #message
            Email, #from Email
            ['mei.proj2122@gmail.com'], #TO Email
        )

        return render (request, "contact.html", {"name": Name})

    else:
        return render (request, "contact.html", {})