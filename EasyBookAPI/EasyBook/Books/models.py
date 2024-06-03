from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Book(models.Model):
    author_name = models.CharField(max_length=50)
    first_publish_year = models.PositiveSmallIntegerField(default=0)
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    first_sentence = models.CharField(max_length=10000)

    def __str__(self):
        return self.title


class BooksReadByUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(null=True)
    note = models.CharField(max_length=2500, null=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.book.title} - {self.user.username} - {self.rating} - {self.note}'


class BooksAbandonedByUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    note = models.CharField(max_length=2500, null=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.book.title} - {self.user.username} - {self.note}'


class BooksToBeReadByUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    note = models.CharField(max_length=2500, null=True)

    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f'{self.book.title} - {self.user.username} - {self.note}'
