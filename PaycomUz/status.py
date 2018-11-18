from PayMe.models import StatusTransaction


ORDER_NOT_FOND = -31050
STATUS_OK = 200
TRANSACTION_NOT_FOND = -31003


def processing():
    get,create = StatusTransaction.objects.get_or_create(text='processing')
    return get

def success():
    get,create = StatusTransaction.objects.get_or_create(text='success')
    return get

def failed():
    get,create =  StatusTransaction.objects.get_or_create(text='failed')
    return get

def cancel():
    get,create = StatusTransaction.objects.get_or_create(text='cancel')
    return get

