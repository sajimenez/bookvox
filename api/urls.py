from django.urls import path, include
from rest_framework.authtoken import views as views_r
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('books', views.BookViewSet)

app_name = 'api'

urlpatterns = [
    path('auth/', views_r.obtain_auth_token),
    path('', include(router.urls))
]
