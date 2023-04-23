from django.urls import path, include
from animals.views import animals, animal_detail, buy_animal, fine, delete_animal, create_animal

urlpatterns = [
    path('', animals, name='animals'),
    path('animals/<int:animal_id>/', animal_detail, name='animal_detail'),
    path('buy_animal/<int:animal_id>/', buy_animal, name="buy_animal"),
    path('fine/', fine, name='fine'),
    path('delete_animal/<int:animal_id>/', delete_animal, name="delete_animal"),
    path('create_animal/', create_animal, name="create_animal"),

]
