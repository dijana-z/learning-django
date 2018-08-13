from rest_framework import serializers
from .models import Stock


class StockSerializer(serializers.ModelSerializer):
    """
    Converts the model to JSON file
    """

    class Meta:
        # what model are you serializing?
        model = Stock
        # what attributes will you return to the user?
        # fields = ('ticker', 'volume')
        fields = '__all__'
