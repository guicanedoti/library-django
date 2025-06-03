from rest_framework import serializers
from core.models import Book

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']  # Campos resumidos para GET ALL

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Todos os campos para GET by ID

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['id']  # Supondo que o ID é gerado automaticamente

class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year']  # Campos editáveis
