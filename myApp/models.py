from django.db import models

class photos(models.Model):
    title = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/')
    desc = models.TextField(max_length = 255)
    link = models.URLField()
