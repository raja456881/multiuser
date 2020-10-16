from django.db import models

# Create your models here.
from django.db import models
from address.models import AddressField
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel
from datetime import date
from decimal import Decimal
from django.conf import settings
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.
class location1(models.Model):
    country=models.CharField(max_length=30)
    state=models.CharField(max_length=23)
    city=models.CharField(max_length=23)

class Currency(models.Model):
    code = models.CharField(unique=True, max_length=3)
    pre_symbol = models.CharField(blank=True, max_length=1)
    post_symbol = models.CharField(blank=True, max_length=1)

    def __unicode__(self):
        return self.code

class Address(models.Model):
    contact_name=models.CharField(max_length=23)
    address_one=AddressField()
    town=models.CharField(max_length=34)
    postcode=models.CharField(_("zip code"), max_length=5, default="43701")
    state = models.CharField(max_length=34)

class InvoiceManager(models.Manager):
    def get_invoiced(self):
        return self.filter(invoiced=True, draft=False)

    def get_due(self):
        return self.filter(invoice_date__lte=date.today(),
                           invoiced=False,
                           draft=False)







gender=(('M','Male'),('F','Female'),('TS','Transgender'))
class customer(models.Model):
    id = models.AutoField(primary_key=True)
    Customer_name= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Customer_gender = models.CharField(choices=gender,max_length=50)
    Customer_profilepic = models.FileField()
    Customer_Email = models.EmailField(max_length=111)
    Customer_created_at = models.DateTimeField(auto_now_add=True)
    Customer_PhoneNo1 = PhoneNumberField(null=False, blank=False, unique=False)
    Customer_Street=models.CharField(max_length=250,default='')
    Customer_Landmark = models.CharField(max_length=100, default='')
    Customer_Zipcode= models.IntegerField(default='')
    Customer_State = models.CharField(max_length=100, default='')
    Customer_Country = models.CharField(max_length=100, default='')
    objects = models.Manager()



class Invoice(TimeStampedModel):
    user = models.OneToOneField(customer, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=34)
    invoice_id = models.CharField(unique=True, max_length=6, null=True,
                                  blank=True, editable=False)
    invoice_date = models.DateField(default=date.today)
    invoiced = models.BooleanField(default=False)
    draft = models.BooleanField(default=False)
    paid_date = models.DateField(blank=True, null=True)

    objects = InvoiceManager()


    def __unicode__(self):
        return u'%s (%s)' % (self.invoice_id, self.total_amount())

    class Meta:
        ordering = ('-invoice_date', 'id')

    def total(self):
        total = Decimal('0.00')
        for item in self.items.all():
            total = total + item.total()
        return total

    def file_name(self):
        return u'Invoice %s.pdf' % self.invoice_id

class Order(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    email=models.CharField(max_length=111)
    amount=models.IntegerField(default=0)
    phone=models.CharField(max_length=111, default="")
    coursename=models.CharField(max_length=5000)
    prices=models.CharField(max_length=500)
    qty=models.CharField(max_length=400)
    date= models.DateTimeField(default=datetime.now(), blank=True)



