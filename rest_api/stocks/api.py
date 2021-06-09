from .models import stocks
from rest_framework import serializers, viewsets

class StocksSerializer(serializers.ModelSerializer):

    class Meta:
        model=stocks
        fields='__all__'

class StocksViewSet(viewsets.ModelViewSet):
    queryset = stocks.objects.all()
    serializer_class = StocksSerializer