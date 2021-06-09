from .models import books
from rest_framework import serializers, viewsets

class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model=books
        fields='__all__'

class BooksViewSet(viewsets.ModelViewSet):
    queryset = books.objects.all()
    serializer_class = BooksSerializer