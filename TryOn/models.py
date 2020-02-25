from django.db import models
from TryOnProtoType import settings


class Vendor(models.Model):
    name = models.CharField(max_length=30)
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


class Product(models.Model):
    vendor_id = models.BigIntegerField()
    brand = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    sub_category = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=10) # top or bottom
    material = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=6)


class ProductReview(models.Model):
    pid = models.BigIntegerField()
    cid = models.BigIntegerField()
    review = models.CharField(max_length=500)
    product_rating = models.BigIntegerField()
    vendor_rating = models.BigIntegerField()


class ProductStock(models.Model):
    pid = models.BigIntegerField()
    uid = models.BigIntegerField()
    color = models.CharField(max_length=20)
    size = models.BigIntegerField()
    quantity = models.BigIntegerField()


class ProductImages(models.Model):
    pid = models.BigIntegerField()
    image = models.BinaryField()

class ProductReviewImage(models.Model):
    rid = models.BigIntegerField()
    image = models.BinaryField()

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
