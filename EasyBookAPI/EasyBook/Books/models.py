from django.db import models

# Create your models here.

class Book(models.Model):
    author_name = models.CharField(max_length=50)
    first_published_year = models.PositiveSmallIntegerField(default=0)
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    first_sentence = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=200)
    currently_reading = models.CharField(max_length=100)
    favourite_book = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.username

class BooksReadByUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(null=True)
    note = models.CharField(max_length=2500, null=True)

    def __str__(self):
        return f'{self.book.title} - {self.user.username}'

class BooksAbandonedByUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    note = models.CharField(max_length=2500, null=True)

    def __str__(self):
        return f'{self.book.title} - {self.user.username}'

class BooksToBeReadByUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    note = models.CharField(max_length=2500, null=True)

    def __str__(self):
        return f'{self.book.title} - {self.user.username}'