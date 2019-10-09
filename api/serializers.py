from rest_framework import serializers

from core.models import Category, Book


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for the Category object"""
    class Meta:
        model = Category
        fields = ('id', 'name')


class BookSerializer(serializers.ModelSerializer):
    """Serializer for the Book object"""
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Book
        fields = (
            'id',
            'category_id',
            'title',
            'thumbnail_url',
            'price',
            'stock',
            'product_description',
            'upc',
        )
