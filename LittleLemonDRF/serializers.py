from rest_framework import serializers
from .models import Book, AuthorDet

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorDet
        fields = ['id','gender','age']

class BookListSerializer(serializers.HyperlinkedModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price = serializers.SerializerMethodField(method_name='multiple')
    authordet = AuthorSerializer(read_only=True)
    # authordet = serializers.HyperlinkedRelatedField(
    #     queryset = AuthorDet.objects.all(),
    #     view_name = 'author-detail'
    # )
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'price', 'stock','authordet']
        depth=1

    def multiple(self,product:Book):
        return product.price*10
