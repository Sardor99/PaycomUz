from django.urls import path
from .views import MerchantAPIVIew



urlpatterns = [

   path('paycom',MerchantAPIVIew.as_view())

]