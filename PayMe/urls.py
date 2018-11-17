from django.urls import path
from .views import MerchantAPIVIew



urlpatterns = [

   path('pay/me',MerchantAPIVIew.as_view())

]