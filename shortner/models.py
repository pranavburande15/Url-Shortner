from django.db import models

class ShortURL(models.Model):
    long_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=10, unique=True)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.short_code