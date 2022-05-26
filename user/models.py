from django.db import models
from book.models import BookItem

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.last_name} | ID: {self.id}"


class UserRequest(models.Model):
    book = models.ForeignKey(BookItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent = models.BooleanField(default=False)
    reserve = models.BooleanField(default=False)

    def __str__(self):
        return f"Book: ({self.book})  |  User: ({self.user})  |  Rent: {self.rent} | Reserve: {self.reserve}"
