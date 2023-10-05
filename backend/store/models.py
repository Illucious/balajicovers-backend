from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField()
    image = models.ImageField(upload_to='images/categories/')
    def __str__(self):
        return self.name
    
class SubCategories(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField()
    # image = models.ImageField(upload_to='images/categories/')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/products/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    def __str__(self):
        return self.name