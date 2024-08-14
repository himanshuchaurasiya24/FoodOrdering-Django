from django.db import models
import uuid
# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created_at= models.DateField(auto_created=True)
    updated_at= models.DateField(auto_created=True)
    # to treat this class as class and not as a model write the below code...
    class Meta:
        abstract=True
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_slug = models.SlugField(unique=True)
    product_description = models.TextField(unique=True)
    product_price = models.IntegerField(default=0)
class ProductImages(models.Model):
    product_image = models.CharField(max_length=100)
class DummyModel(models.Model):
    pass
