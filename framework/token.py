from rest_framework.authtoken.models import Token

def prodToken():
    token = Token.objects.create()
    return token