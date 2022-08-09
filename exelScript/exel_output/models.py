from django.db import models

# Create your models here.


class Uploader(models.Model):
    first_exel_file = models.FileField(upload_to="exel/")
    second_exel_file = models.FileField(upload_to="exel/")
    out_file = models.FileField(upload_to="out/", null=True)


class Photo(models.Model):
    images = models.ImageField(upload_to="images", null=True)