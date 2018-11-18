# **DJANGO RESTFRAMEWORK PAYCOMUZ 🇺🇿**

```
pip install Django
pip install Djangorestframework
pip install PaycomUz
```
**settings.py**
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
**settings.py**
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