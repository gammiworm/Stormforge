from django.urls import path
from .views import handleCRUD

urlpatterns = [
    path("crud/", handleCRUD, name="handleCRUD"),
]