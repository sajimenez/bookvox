from django.db import models


class Category(models.Model):
    """Model representing a book category"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Book(models.Model):
    """Model representing a book"""
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(max_length=255)
    thumbnail_url = models.URLField(max_length=255, null=True)
    price = models.CharField(max_length=255, null=True)
    stock = models.BooleanField()
    product_description = models.TextField(null=True)
    upc = models.CharField(max_length=255, unique=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
