from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class DataModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=500)
    slug = models.CharField(max_length=500)
    clicked = models.IntegerField(default=0, null=True, blank=True)
    date  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Short url form: {self.url} is {self.slug}'
