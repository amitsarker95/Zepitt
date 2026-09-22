from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=40)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

