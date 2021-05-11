from django.db import models

class DataModel(models.Model):
    url = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    def __str__(self):
        return f'Short url forL: {self.url} is {self.slug}'
