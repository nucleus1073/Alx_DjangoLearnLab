from django.urls import include, path 
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
     path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the api.urls for routing to the api app
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), # Token authentication endpoint
]