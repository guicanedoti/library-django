from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import (
    HomePageView,
    AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    BookListView, BookCreateView, BookUpdateView, BookDeleteView, BookDetailView,
    LoanListView, LoanCreateView, LoanUpdateView, delete_author
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), 
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', delete_author, name='author-delete'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    path('loans/', LoanListView.as_view(), name='loan-list'),
    path('loans/create/', LoanCreateView.as_view(), name='loan-create'),
    path('loans/<int:pk>/update/', LoanUpdateView.as_view(), name='loan-update'),
]
