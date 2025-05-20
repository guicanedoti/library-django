from rest_framework.routers import DefaultRouter
from core.serializers.book_serializer import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = router.urls
