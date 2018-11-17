from django.conf import settings
accounts_key = settings.PAYME_SETTINGS['ACCOUNTS']


def CheckPerformTransaction_key(data):
    if accounts_key['KEY2'] == False:
        id = data['params']['account'][accounts_key['KEY1']]
        amount = data['params']['amount']
        return id,amount,None

    else:
        id = data['params']['account'][accounts_key['KEY1']]
        type = data['params']['account'][accounts_key['KEY2']]
        amount = data['params']['amount']
        return id,amount,type

def CreateTransaction_key(data):
    if accounts_key['KEY2'] == False:
        account_id = data['params']['account'][accounts_key['KEY1']]
        amount = data['params']['amount']
        time = data['params']['time']
        id = data['params']['id']
        key = {"id": id, "time": time, "amount": amount,"account_id": account_id,"account_type":None}
        return key

    else:
        account_id = data['params']['account'][accounts_key['KEY1']]
        account_type = data['params']['account'][accounts_key['KEY2']]
        amount = data['params']['amount']
        time = data['params']['time']
        id = data['params']['id']
        key = {"id":id,"time":time,"amount":amount,"account_type":account_type,"account_id":account_id}
        return key


def PerformTransaction_key(data):
    id = data['params']['id']
    return id