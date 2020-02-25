from django.db import models


class Customer(models.Model):
    f_name = models.CharField(max_length=30)
    m_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    referral = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    pincode = models.BigIntegerField()
    state = models.CharField(max_length=30)


class CustomerInterest(models.Model):
    search_date = models.DateField()
    pid = models.BigIntegerField()
    uid = models.BigIntegerField()


class Cart(models.Model):
    cartid = models.BigIntegerField()
    category = models.CharField(max_length=120)
    price = models.IntegerField()
    imgeurl = models.CharField(max_length=250)
    quantity = models.IntegerField()
