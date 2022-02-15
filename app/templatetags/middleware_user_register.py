
from tweets import queries


## This class is responsible for adding a user to the database whenever a new session is started.

class UserRegister:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self,request) :
        response = self.get_response (request)
        
        if request.session.get('id_user') and queries.get_participante (request.session.get('id_user')) is not None :
            print(" [Session] Este utilizador ja tem session")

        
        else:
            ## creat session with the user id
            id, message = queries.add_participant()
            request.session['id_user'] = id
          ##  print(id)
          ##  print(message)

        return response