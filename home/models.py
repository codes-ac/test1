from django.db import models
from django.urls import reverse


class General_Enquiry(models.Model):
    name      = models.CharField(max_length=100)
    email     = models.EmailField(max_length=254)
    subject   = models.CharField(max_length=300)
    message   = models.TextField()

    def __str__(self):
        return self.name


class Gallery(models.Model):
    image     = models.ImageField( upload_to="achievement", blank=True, null=True)
    desc      = models.CharField(max_length=250, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class ATL_Lab_Picture(models.Model):
    image     = models.ImageField( upload_to="atl", blank=True, null=True)
    desc      = models.CharField(max_length=250, blank=True, null=True)


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class Product(models.Model):
    name      = models.CharField(max_length=100, blank=True, null=True)
    image     = models.ImageField( upload_to="showcase", blank=True, null=True)
    desc      = models.CharField(max_length=250, blank=True, null=True)
    price     = models.CharField(max_length=100, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url
    
    def __str__(self):
        return self.name
    

    
class Staff(models.Model):
    image         = models.ImageField( upload_to="team", blank=True, null=True)
    name          = models.CharField(max_length=250, blank=True, null=True)
    desg          = models.CharField(max_length=250, blank=True, null=True)
    qualification = models.CharField(max_length=300, blank=True, null=True)
    doj           = models.DateTimeField(blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.name


class eSamachar(models.Model):
    image     = models.ImageField( upload_to="achievement", blank=True, null=True)
    desc      = models.CharField(max_length=250, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url


class OrderQuery(models.Model):
    product       = models.CharField(max_length=250, blank=True, null=True)


class Notice_Board(models.Model):
    name   = models.CharField(max_length=300, blank=True, null=True)
    link   = models.CharField(max_length=3000, blank=True, null=True)
    notice = models.FileField(null=True, blank=True, upload_to="notice")
    date   = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f'{self.name}'

    @property
    def noticeURL(self):
        try:
            url = self.notice.url
        except:
            url = ""
        return url

    

class Order(models.Model):
    product   = models.CharField(max_length=100)
    orderId   = models.CharField(max_length=100)
    email     = models.EmailField(max_length=254)
    quantity  = models.CharField(max_length=300)
    mobile    = models.CharField(max_length=300, default="")
    name      = models.CharField(max_length=300, default="")
    address   = models.CharField(max_length=300, default="")
    pincode   = models.CharField(max_length=300, default="")


    def __str__(self):
        return f'{self.product} by {self.email}'





    
