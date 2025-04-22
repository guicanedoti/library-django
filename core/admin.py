from django.contrib import admin
from .models import Author
from .models import Book
from .models import Category
from .models import Loan

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Loan)