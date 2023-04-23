from django.urls import path, include
from items.views import items, delete_item

urlpatterns = [
    path('items/', items, name='items'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),

]
