from django.contrib import admin
from .models import Transaction
# Register your models here.

class TransactionMyAdmin(admin.ModelAdmin):
    list_display = ('id','transaction_id', 'account_id', 'account_type','price','status','date')
    list_display_links = ('id',)
    list_filter = ('_id', 'account_id', 'status','time')
    search_fields = ['transaction_id', 'status','error','time']

    @staticmethod
    def price(obj):
        return "{} {}".format(obj.amount, '$')
    @staticmethod
    def transaction_id(obj):
        return "{}".format(obj._id)

admin.site.register(Transaction,TransactionMyAdmin)