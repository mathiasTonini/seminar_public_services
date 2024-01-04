import jwt
import datetime

def create_jwt(payload, secret_key):
    # Set the expiration time for the JWT (e.g., 30 minutes from now)
    exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    # Create the JWT
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

def checkLogin(username, password):
    return True