from django.db import models

# Create your models here.


class Category(models.Model):
    content = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    img = models.ImageField()

    def __str__(self):
        return f"{self.content}"


class SubCategory(models.Model):
    content = models.CharField(max_length=128)
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    img = models.ImageField()

    def __str__(self):
        return f"{self.content}"


class Product(models.Model):
    name = models.CharField(max_length=128)
    subctg = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    discription = models.CharField(max_length=512)
    brand = models.CharField(max_length=128)
    on_complect = models.CharField(max_length=128)
    uzunlik = models.CharField(max_length=128)
    kenglik = models.CharField(max_length=128)
    balandlik = models.CharField(max_length=128)
    img = models.ImageField()

    def __str__(self):
        return f"{self.name}"
