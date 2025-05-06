from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    fullname = models.CharField(max_length=100)
    birthdate = models.DateField(auto_now_add=False)
    rating = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ['fullname']


class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year_published = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.title
    
    @property
    def short_description(self):
        return (self.description[:50] + '...') if self.description and len(self.description) > 50 else self.description


class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    returned = models.BooleanField(default=False) 
    
    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'
    
    
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"

    def __str__(self):
        return self.name