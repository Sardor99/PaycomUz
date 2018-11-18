#DJANGO-RESTFRAMEWORK-PAYCOM-UZ

```
pip install Django
pip install Djangorestframework
pip install PaycomUz
```

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework`,
    'PaycomUz`
]

```
```
python manage.py migrate
```

```
PAYME_SETTINGS = {
    "HOST":"https://checkout.test.paycom.uz/api",   #test host
    "ID":"<<API TOKEN>>",          #token
    "SECRET_KEY":"<<API SECRET KEY>>",  #password
    "PATH_CHECK_PERFORM_TRANSACTION":"<<path function>>",  #check order
    "PATH_SUCCESS_FUNCTION":"<<path function>>",
    "PATH_ERROR_FUNCTION":"<<path function>>",
    "ACCOUNTS":{
        "KEY1":"id",
        "KEY2":False #or "type"
    }
}
```