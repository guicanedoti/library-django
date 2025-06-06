from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import viewsets
from .serializers.book_serializer import (
    BookListSerializer,
    BookDetailSerializer,
    BookCreateSerializer,
    BookUpdateSerializer,
)

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
    

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        elif self.action == 'retrieve':
            return BookDetailSerializer
        elif self.action == 'create':
            return BookCreateSerializer
        elif self.action in ['update', 'partial_update']:
            return BookUpdateSerializer
        return BookDetailSerializer  # fallback


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_details.html', {'book': book})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'book_form.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'book_confirm_delete.html', {'book': book})

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
