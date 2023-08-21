from rest_framework import serializers
from .models import Book
from django.forms import ValidationError

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = ('id', 'title', 'number_of_pages', 'quantity', 'price')
        fields = '__all__'
    
    # valided_data is a dictionary of deserialized data
    
    def validate_title(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Title is too short")
        return value
    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative")
        return value
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative")
        return value
    def validate(self, data):
        if data['quantity'] > 100:
            raise serializers.ValidationError("Quantity cannot be greater than 100")
        return data
    
    
    
    