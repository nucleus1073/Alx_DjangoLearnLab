from django.contrib import admin
from django.urls import include, path
from django.urls import include, path
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api.urls for routing to the api app
]
# Set up the router for the viewset
router = DefaultRouter()
router.register(r'books', BookViewSet)

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include the router URLs
    path('books/', BookList.as_view(), name='book-list'),  # View for listing books
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token authentication
]
