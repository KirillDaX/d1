from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Product(models.Model):
    """ товар """
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='static')

    def __str__(self):
        return self.title


class Reviews(models.Model):
    """ отзывы """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    rate = models.PositiveIntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    body_text = models.TextField(max_length=500)


class Article(models.Model):
    """ статьи """
    title = models.CharField(max_length=100)
    body_text = models.TextField(max_length=500)
    creation_date = models.DateField(auto_now_add=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)  # товары которые будут в статьте.

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-creation_date']
