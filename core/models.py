from django.db import models


class Category(models.Model):
    """Model representing a book category"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Book(models.Model):
    """Model representing a book"""
    category_id = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(max_length=255)
    thumbnail_url = models.URLField(max_length=255)
    price = models.CharField(max_length=255)
    stock = models.BooleanField()
    product_description = models.TextField()
    upc = models.CharField(max_length=255)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
