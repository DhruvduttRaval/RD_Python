from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	address=models.TextField()
	city=models.CharField(max_length=100)
	zipcode=models.PositiveIntegerField()
	mobile=models.PositiveIntegerField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to="profile_pic/")
	usertype=models.CharField(max_length=100,default="user")

	def __str__(self):
		return self.fname +" "+ self.lname

class Product(models.Model):
	CHOICE=(
		('Laptop','Laptop'),
		('Accessories','Accessories'),
		('Camera','Camera'),
		)
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_category=models.CharField(max_length=100,choices=CHOICE)
	product_name=models.CharField(max_length=100)
	product_price=models.PositiveIntegerField()
	product_desc=models.TextField()
	product_image=models.ImageField(upload_to="product_image/")

	def __str__(self):
		return self.seller.fname+"- "+self.product_category

class Wishlist(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.fname+"-"+self.product.product_name