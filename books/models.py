from django.db import models

class Book(models.Model):
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        get_latest_by = 'created_at'

    title = models.CharField(max_length=80)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
