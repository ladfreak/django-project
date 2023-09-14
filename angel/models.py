from django.db import models
from datetime import datetime
import os
from django.contrib.auth.models import User


# Create your models here.

def image(request,filename):
    time=datetime.now().strftime("%Y%m%d,%H:%M:%S")
    get_image="%s%s"%(time,filename)
    return get_image
    
class catagory(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=image,null=True,blank=True)
    discription=models.TextField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class product(models.Model):
    catagory=models.ForeignKey(catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to=image,null=True,blank=True)
    discription=models.TextField(null=False,blank=False)
    orignal_price=models.FloatField(null=True,blank=True)
    selling_price=models.FloatField(null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    treanding=models.BooleanField(default=False,help_text="0-default,1-treanding")   
    status=models.BooleanField(default=False,help_text="0-show,1-hidden")
    created_at=models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    product_quantity=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_quantity*self.product.selling_price

class fav(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    
