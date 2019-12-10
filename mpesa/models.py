from django.db import models

# Create your models here.
class Stk(models.Model):
    MerchantRequestID = models.TextField(blank=True)
    CheckoutRequestID =models.TextField(blank=True)
    ResultCode = models.TextField(blank=True)
    ResultDesc= models.TextField(blank=True)
    amount = models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
    MpesaReceiptNumber = models.TextField(blank=True)
    TransactionDate = models.DateField(blank=True, null=True)
    PhoneNumber = models.TextField(blank=True)
    Balance = models.DecimalField(max_digits=7,decimal_places=2,default=0.00)
