from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .models import Author, Category, Book, Loan

# Página Inicial 

class HomePageView(TemplateView): 
    template_name = 'home.html'

# Autores

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['fullname', 'nationality']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author-list')


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    fields = ['fullname', 'nationality']
    template_name = 'author_form.html'
    success_url = reverse_lazy('author-list')


class AuthorDeleteView(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'author_confirm_delete.html'
    success_url = reverse_lazy('author-list')



# Categorias

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name', 'gener']
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name', 'gener']
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('category-list')



# Livros

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'year_published', 'category', 'description']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')


class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'year_published', 'category', 'description']
    template_name = 'book_form.html'
    success_url = reverse_lazy('book-list')


class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book-list')



# Empréstimos

class LoanListView(LoginRequiredMixin, ListView):
    model = Loan
    template_name = 'loan_list.html'
    context_object_name = 'loans'

    def get_queryset(self):
        return Loan.objects.filter(user=self.request.user)


class LoanCreateView(LoginRequiredMixin, CreateView):
    model = Loan
    fields = ['book']
    template_name = 'loan_form.html'
    success_url = reverse_lazy('loan-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LoanUpdateView(LoginRequiredMixin, UpdateView):
    model = Loan
    fields = ['return_date', 'returned']
    template_name = 'loan_form.html'
    success_url = reverse_lazy('loan-list')
