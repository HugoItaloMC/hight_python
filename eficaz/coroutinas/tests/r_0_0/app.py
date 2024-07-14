from __init__ import api
from schema import Schema

if __name__ == '__main__':
    api(Schema, 'POST', 'nameHugo', 'passwdHugo', 'emailHugo')
    #print(api(Schema, 'GET', 'nameHugo', 'passwdHugo', 'emailHugo'))