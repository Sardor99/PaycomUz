#PayMe

**settings.py**
```
PAYME_SETTINGS = {
    "HOST":"https://checkout.test.paycom.uz/api",   #test host
    "ID":"<<API TOKEN>>",          #token
    "SECRET_KEY":"<<PASSWORD KEY>>",  #password
    "PATH_CHECK_PERFORM_TRANSACTION":"<<path function>>",  #check order
    "PATH_SUCCESS_FUNCTION":"<<path function>>",  #update order
    "PATH_ERROR_FUNCTION":"<<path function>>", #error order
    "ACCOUNTS":{
        "KEY1":"id",
        "KEY2":"type"
        }
```
**your function**
```
from PayMe.status import STATUS_OK , ORDER_NOT_FOND

def perform_check(id=0,type='',amount=0)
    #check order
    return STATUS_OK or return ORDER_NOT_FOND
```

```
def update_order(id='')
    #order update succsess
```

```
def error_order(id='')
   #order status faield
```
