from django.shortcuts import render
from items.models import Items, ItemsCategory
from django.shortcuts import get_object_or_404, redirect

def items(request):
    items = Items.objects.all()
    return render(request, "items.html", {"items": items})


def delete_item(request, item_id):
    item = get_object_or_404(Items, pk=item_id)
    item.delete()
    return redirect('items')