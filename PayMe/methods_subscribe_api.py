import requests
import json
from django.conf import settings
from .models import Transaction
import time
from .status import failed
from importlib import import_module

HOST = settings.PAYME_SETTINGS['HOST']  #URL PAYME

AUTHORIZATION = settings.PAYME_SETTINGS['ID']  #TOKEN

HEADERS = {'Content-type': 'application/json' , 'X-Auth':AUTHORIZATION} #HEADERS

accounts_key = settings.PAYME_SETTINGS['ACCOUNTS']




def receipts_create(id=0,price=0.00,token='',type=''):
    response = {
        "id": 123,
        "method": "receipts.create",
        "params": {
            "amount":price * 100,
            "account": {
                accounts_key['KEY1']:id,
                accounts_key['KEY2']:type
            }
        }
    }
    try:
        r = requests.post(HOST, data=json.dumps(response), headers=HEADERS)
        data = json.loads(r.text)
        if 'error' in data:
            print(data)
            error = Transaction.objects.create(
                _id="000000000000000000000",
                account_id=id,
                account_type=type,
                time=time.time(),
                amount=price,
                state=0,
                status=failed(),
                error=data['error'],
                request_id='401'
            )
            import_settings = import_module(settings.PAYME_SETTINGS['PATH_ERROR_FUNCTION'])
            error_transaction = import_settings.error_order(id=error.id)
            return False
        else:
            receipts_pay(id=data['result']['receipt']['_id'],token=token)
    except:
        print("SERVER ERROR 500")



def receipts_pay(id='',token=''):
    response = {
        "id": 123,
        "method": "receipts.pay",
        "params": {
            "id": id,
            "token":token
        }
    }
    try:
        r = requests.post(HOST, data=json.dumps(response), headers=HEADERS)
        data = json.loads(r.text)
        if 'error' in data:
            print(data)
            try:
                error_transaction = Transaction.objects.get(_id=id)
                error_transaction.status = failed()
                error_transaction.state = 0
                error_transaction.error = data['error']
                error_transaction.save()

                import_settings = import_module(settings.PAYME_SETTINGS['PATH_ERROR_FUNCTION'])
                error = import_settings.error_order(id=error_transaction.id)
            except Transaction.DoesNotExist:
                print("TRANSACTION NOT FOND")
            return False
        else:
            import_settings = import_module(settings.PAYME_SETTINGS['PATH_SUCCESS_FUNCTION'])
            success = import_settings.update_order(id=id)

    except:
        try:
            error_transaction = Transaction.objects.get(_id=id)
            error_transaction.status = failed()
            error_transaction.state = 0
            error_transaction.error = 'SERVER ERROR 500'
            error_transaction.save()

            import_settings = import_module(settings.PAYME_SETTINGS['PATH_ERROR_FUNCTION'])
            error = import_settings.error_order(id=error_transaction.id)
        except Transaction.DoesNotExist:
            print("TRANSACTION NOT FOND")
            return False

