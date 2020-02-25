from django.db import models


class Shipper(models.Model):
    sname = models.CharField(max_length=30)
    owner_fname = models.CharField(max_length=30)
    owner_lname = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    mobile = models.BigIntegerField()
    email = models.TextField(max_length=50)
    business_address = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    pincode = models.BigIntegerField()
    zone = models.CharField(max_length=30)
    gst_no = models.CharField(max_length=15)
    aadhar_no = models.BigIntegerField()
    tradelicense_id = models.BigIntegerField()
    permit_document = models.FileField(upload_to="Files")
    address_proof = models.FileField(upload_to="Files")
    request_status = models.BooleanField(default=False)


class Order(models.Model):
    cid = models.BigIntegerField()
    address = models.CharField(max_length=120)
    payment_mode = models.CharField(max_length=20)
    pid = models.BigIntegerField()
    productType = models.CharField(max_length=10)
    productsize = models.BigIntegerField()
    productColour = models.CharField(max_length=20)
    vendor_id = models.BigIntegerField()
    # vendor_id = models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    total_amount = models.BigIntegerField()
    status = models.CharField(max_length=25)
    shipper_id = models.BigIntegerField()
    # shipper_id = models.ForeignKey(Shipper, on_delete=models.DO_NOTHING)
