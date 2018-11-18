import base64
from django.conf import settings


def decode(key):
    try:
        token = key.split('Basic')
        decode_key = base64.b64decode(token[1])
        secret_key = str(decode_key,'utf-8').split('Paycom:')
        if secret_key[1] == settings.PAYME_SETTINGS['SECRET_KEY']:
            return True
        else:
            return False
    except:
        return False

