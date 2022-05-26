from django.db import models
from book.models import Book

# Create your models here.


class Shelf(models.Model):
    category = models.CharField(max_length=50)
    books = models.ManyToManyField(Book, null=True)

    def __str__(self):
        return f"Category: {self.category} | N°: {self.id}"
