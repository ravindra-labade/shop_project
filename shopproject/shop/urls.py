from django.urls import path
from .views import add_shop, show_shop, update_shop, delete_shop


urlpatterns = [
    path('add/', add_shop, name='add_url'),
    path('show/', show_shop, name='show_url'),
    path('update/<int:pk>/', update_shop, name='update_url'),
    path('delete/<int:pk>/', delete_shop, name='delete_url'),
]
