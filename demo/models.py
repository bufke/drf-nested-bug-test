from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)


class BookSnippet(models.Model):
    book = models.ForeignKey(Book)
    snippet = models.CharField(max_length=100)
