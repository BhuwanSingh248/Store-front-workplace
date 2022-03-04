from django.db import models


class Company(models.Model):
    company_id  = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    description = models.TextField()

class product(models.Model):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=50)
    product_description  = models.TextField()
    company = models.ForeignKey(Company, on_delete= models.CASCADE)

    
class Inventory(models.Model):
    category = models.SmallIntegerField()
    product = models.ForeignKey(product, related_name='productName', on_delete=models.CASCADE)
    mnm = models.ManyToManyField('product', related_name='productCompany')