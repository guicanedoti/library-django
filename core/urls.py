from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from .views import (
    HomePageView,
    AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    book_list, book_detail, book_create, book_update, book_delete,
    LoanListView, LoanCreateView, LoanUpdateView, delete_author
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'), 
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('api/', include('core.api_urls')),

    path('authors/', AuthorListView.as_view(), name='author-list'),
    path('authors/create/', AuthorCreateView.as_view(), name='author-create'),
    path('authors/<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),
    path('authors/<int:pk>/delete/', delete_author, name='author-delete'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    path('books/', book_list, name='book-list'),
    path('books/create/', book_create, name='book-create'),
    path('books/<int:pk>/update/', book_update, name='book-update'),
    path('books/<int:pk>/delete/', book_delete, name='book-delete'),
    path('books/<int:pk>/', book_detail, name='book-detail'),

    path('loans/', LoanListView.as_view(), name='loan-list'),
    path('loans/create/', LoanCreateView.as_view(), name='loan-create'),
    path('loans/<int:pk>/update/', LoanUpdateView.as_view(), name='loan-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
