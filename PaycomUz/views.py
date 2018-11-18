from rest_framework.parsers import JSONParser
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.views import APIView
from importlib import import_module
from rest_framework.response import Response
from .status import processing,success
from .models import Transaction
from django.conf import settings
import time
from .status import TRANSACTION_NOT_FOND
from .pars_json_key import CheckPerformTransaction_key,CreateTransaction_key,PerformTransaction_key
from .status import STATUS_OK,ORDER_NOT_FOND
from .password import decode
from .methods_subscribe_api import receipts_create



@authentication_classes([])
@permission_classes([])
class MerchantAPIVIew(APIView):
    def post(self,request):
        if decode(request.META['HTTP_AUTHORIZATION']):
            parser_classes = JSONParser
            API_METHOD = request.data['method']
            if API_METHOD == 'CheckPerformTransaction':
                id,amount,type = CheckPerformTransaction_key(request.data)
                import_settings = import_module(settings.PAYME_SETTINGS['PATH_CHECK_PERFORM_TRANSACTION'])
                status = import_settings.check_perform(id=id,amount=amount,type=type)
                if status == STATUS_OK:
                    return Response({
                       "result": {
                             "allow": True
                         }
                     })
                else:
                    data = {"error": {
                        "code": status,
                        "id": request.data['id'],
                        "message": {
                            "ru": "order не найден "
                        }
                    }}
                    return Response(data)
            elif API_METHOD == 'CreateTransaction':
                key = CreateTransaction_key(request.data)
                id = CreateTransaction(request_id=request.data['id'],
                                       account_id=key['account_id'],
                                       account_type=key['account_type'],
                                       amount=key['amount'],
                                       time=key['time'],
                                       _id=key['id']
                                       ).Create()
                return Response(
                    {
                        "result": {
                            "create_time": key['time'],
                            "transaction": str(id),
                            "state": 1
                        }
                    }
                )
            elif API_METHOD == 'PerformTransaction':
                id = PerformTransaction_key(request.data)
                pk = CreateTransaction(_id=id).Perform()
                if pk == False:
                    data = {"error": {
                        "code": TRANSACTION_NOT_FOND,
                        "id": request.data['id'],
                        "message": {
                            "ru": "транзакция не найден "
                        }
                    }}
                    return Response(data)
                else:
                    date_time = lambda: int(round(time.time() * 1000))
                    return Response({
                        "result":{
                            "transaction":str(pk),
                            "state":2,
                            "perform_time":date_time()
                        }
                    })
            else:
                return Response({
                    "code":401
                })
        else:
            return Response({
                "code":401
            })



class CreateTransaction:
    def __init__(self,request_id='',_id=0,account_id=0,account_type='',amount=0,time=0):

        self.request_id = request_id
        self._id = _id
        self.account_id = account_id
        self.account_type = account_type
        self.amount = amount
        self.time = time


    def Create(self):
        get,created = Transaction.objects.get_or_create(
            request_id=self.request_id,
            _id=self._id,
            account_id=self.account_id,
            account_type=str(self.account_type),
            amount=self.amount/100,
            time=self.time,
            state=1,
            status=processing()
        )
        return get.id


    def Perform(self):
        try:
            perform = Transaction.objects.get(_id=self._id)
            if perform.status == processing():
                perform.status = success()
                perform.state = 2
                perform.save()
                return perform.pk

            elif perform.status == success():
                return perform.pk

            else:
                return False
        except Transaction.DoesNotExist:
            return False

    def cancel(self):
        pass

