from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=64)
    image = models.ImageField(upload_to="images/")
    upload_date = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)