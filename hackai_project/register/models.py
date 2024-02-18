from django.db import models


# Create your models here.
class Image(models.Model):
    file = models.ImageField(upload_to="images")
    ImageName = models.CharField(max_length=25, name="Name", default="New File")
