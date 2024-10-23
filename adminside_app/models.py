from django.db import models

# Create your models here.
class CategoryTable(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    category_image = models.ImageField(upload_to='category_images/',blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.category_name