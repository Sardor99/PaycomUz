ORDER_NOT_FOND = -31050   #order topilmadi
MONEY_AMOUNT_DOES_NOT_MATCH = -31001     #orderi narxi tori kemadi
TRANSACTION_NOT_FOND = -31003             #transaction topilmadi
TRANSACTION_HAS_EXPIRED = -31008               #transaction vaqti otib ketdi yoki tolanib yopilgan
TRANSACTION_CANNOT_BE_CANCELLED = -31007               #tranzaksiyani bekor qilb bolmaydi








def error_response(type,request_id=0):
    if type == -31050:
        data = {"error":{
            "code":ORDER_NOT_FOND,
            "id":request_id,
            "message":{
                "ru":"order не найден "
            }
        }}
        return data
    elif type == -31001:
        data = {"error":{
            "code":MONEY_AMOUNT_DOES_NOT_MATCH,
            "id":request_id,
            "message":{
                "ru":"недостаточно средств",
            }
        }}
        return data
    elif type == -31008:
        data = {"error": {
            "code": TRANSACTION_HAS_EXPIRED,
            "id": request_id,
            "message": {
                "ru": "транзакция уже закрыта",
            }
        }}
        return data
    elif type == -31003:
        data = {"error": {
            "code": TRANSACTION_NOT_FOND,
            "message": {
                "uz": "transaction yoq",
                "ru": "транзакция не найден ",
                "en": "transaction not fond"
            }
        }}
        return data
    elif type == -31007:
        data = {"error": {
            "code": TRANSACTION_CANNOT_BE_CANCELLED,
            "message": {
                "ru": "Невозможно отменить транзакцию.  "
            }
        }}
        return data
