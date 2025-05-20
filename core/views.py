from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Author, Category, Book, Loan
from .forms import (BookForm, AuthorForm)

class HomePageView(TemplateView): 
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_books'] = Book.objects.all().order_by('-id')[:12]
        context['top_authors'] = Author.objects.all().order_by('-rating')[:5]
        return context


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'
    context_object_name = 'authors'
    

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_details.html'
    context_object_name = 'author'


class AuthorCreateView(LoginRequiredMixin, CreateView):
    model = Author
    template_name = 'author_form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author-list')


class AuthorUpdateView(LoginRequiredMixin, UpdateView):
    model = Author
    template_name = 'author_form.html'
    form_class = AuthorForm
    success_url = reverse_lazy('author-list')


def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return HttpResponseRedirect(reverse('author-list'))


# Categorias
class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
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
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_details.html'
    context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('book-list')
    
    def form_valid(self, form):
        form.instance = form.save(commit=False)
        if self.request.FILES:
            form.instance.cover = self.request.FILES['cover']
        return super().form_valid(form)

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('book-list')
    
    def form_valid(self, form):
        form.instance = form.save(commit=False)
        if self.request.FILES:
            form.instance.cover = self.request.FILES['cover']
        return super().form_valid(form)
    
    
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return HttpResponseRedirect(reverse('book-list'))


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
