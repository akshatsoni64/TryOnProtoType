from django.db import models


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


class Product(models.Model):
    vendor_id = models.BigIntegerField()
    brand = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    sub_category = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=10)  # top or bottom
    material = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=4)
    # imageurl=models.CharField(max_length=250)


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
    pid = models.ForeignKey(Product, on_delete=models.CASCADE, )
    image = models.CharField(max_length=300)


class ProductReviewImage(models.Model):
    rid = models.BigIntegerField()
    image = models.BinaryField()
