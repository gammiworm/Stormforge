from django.urls import path
from .views import handleCRUD, get_data_points

urlpatterns = [
    path('crud/', handleCRUD, name='handleCRUD'),
    path('get-data-points/', get_data_points, name='get_data_points'),
]