from django.db import models

class ItemsCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Items(models.Model):
    category = models.ForeignKey(ItemsCategory, on_delete = models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=
                              "images", blank=True, null=True)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Items, self).delete(*args, **kwargs)
