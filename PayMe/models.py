from django.db import models

# Create your models here.

class StatusTransaction(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text



class Transaction(models.Model):
    _id = models.CharField(max_length=255)
    request_id = models.CharField(max_length=255)
    account_id = models.IntegerField()        #ORDER ID
    account_type = models.CharField(max_length=255,blank=True,null=True)  #ORDER TYPE
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    state = models.IntegerField(blank=True,null=True)
    time = models.CharField(max_length=255)
    status = models.ForeignKey(StatusTransaction,on_delete=models.CASCADE,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    error = models.TextField(default='None',max_length=255,blank=True,null=True)



