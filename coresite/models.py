from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


# class Category(models.Model):
class Category(MPTTModel):
    """ категория """
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        unique_together = ('slug', 'parent',)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('coresite:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    """ товар """
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=500, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='static', blank=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    slug = models.SlugField(max_length=250, unique=True)
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категория', on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField(verbose_name='В наличии')
    available = models.BooleanField(default=True, verbose_name='Доступно')
    created_item = models.DateTimeField(auto_now_add=True)
    updated_item = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-title']
        index_together = [['id', 'slug']]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('coresite:product_detail', args=[self.id, self.slug])


class Reviews(models.Model):
    """ отзывы """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    rate = models.PositiveIntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)])
    body_text = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Article(models.Model):
    """ статьи """
    title = models.CharField(max_length=100)
    body_text = models.TextField(max_length=500)
    creation_date = models.DateField(auto_now_add=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)  # товары которые будут в статьте.
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-creation_date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


