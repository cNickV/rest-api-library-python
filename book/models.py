from django.db import models
from isbn_field import ISBNField
import datetime

# Create your models here.


class Book(models.Model):
    isbn = ISBNField()
    title = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=80)
    publisher = models.CharField(max_length=80)
    publications_date = models.DateField(default=datetime.date.today, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"Author: {self.author} | Title: {self.title} | Category: {self.category}"
        )


class BookItem(models.Model):
    Book = models.OneToOneField(Book, on_delete=models.CASCADE)
    copies = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.Book} | Copies: {self.copies}"
