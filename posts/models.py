from django.db import models
from django.conf import settings

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=40)
    url = models.URLField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


        

class Vote(models.Model):
    post = models.ForeignKey(
        Posts,
        on_delete=models.CASCADE
    )

    voter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

