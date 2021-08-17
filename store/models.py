from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=200, unique=True, blank=False)
    slug            = models.SlugField(max_length=200, unique=True, blank=False)
    description     = models.TextField(max_length=200, blank=True, null=True)
    price           = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True, editable=False)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_details', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
